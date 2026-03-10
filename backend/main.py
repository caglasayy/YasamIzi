from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, BackgroundTasks
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from firebase_config import initialize_firebase
from pydantic import BaseModel
from typing import List, Optional

from services.ocr_service import ocr_motoru
from services.allergy_analyzer_service import alerji_analiz_motoru, AlerjiRiski
from services.sync_med_service import ilac_takip_motoru
from services.health_nav_service import navigasyon_motoru
from services.life_coach_service import yasam_kocu_motoru
from services.diet_service import diyet_motoru

# Veritabanı tablolarını otomatik oluştur (Geliştirme aşaması için kullanışlıdır)
models.Base.metadata.create_all(bind=engine)

# Firebase entegrasyonunu başlat
initialize_firebase()

app = FastAPI(
    title="Yaşamİzi API",
    description="Sağlık Takibi & Aile Koruyucusu Projesi Merkezi Beyin",
    version="1.0.0"
)

@app.get("/")
def ana_sayfa():
    return {"mesaj": "Yaşamİzi Backend Sistemine Hoş Geldiniz!"}

@app.get("/saglik-durumu")
def saglik_kontrolu():
    """Sistemin ayakta olup olmadığını kontrol eden endpoint"""
    return {"durum": "aktif", "servis": "Yaşamİzi API"}

# Temel bir kullanıcı oluşturma endpoint'i
@app.post("/kullanicilar/")
def kullanici_olustur(ad_soyad: str, eposta: str, firebase_uid: str, db: Session = Depends(get_db)):
    db_kullanici = models.Kullanici(ad_soyad=ad_soyad, eposta=eposta, firebase_uid=firebase_uid)
    db.add(db_kullanici)
    db.commit()
    db.refresh(db_kullanici)
    return db_kullanici

# ---------------------------------------------
# ALERJİ KALKANI (OCR MOTORU & ANALİZ) API'Sİ
# ---------------------------------------------
@app.post("/alerji-kalkani/tara", response_model=AlerjiRiski)
async def urun_tara(dosya: UploadFile = File(...)):
    """
    Kullanıcının gönderdiği ürün/ilaç ambalajı fotoğrafını alır,
    Tesseract OCR ile metinleri çıkartır,
    Alerjen analizi yaparak Risk Seviyesini (KIRMIZI, SARI, YESİL) döner.
    """
    try:
        # Fotoğrafın byte verisini oku
        resim_bytelari = await dosya.read()
        
        # Adım 1: Görselden metni çıkart (OCR)
        okunan_metin = ocr_motoru.resimden_metin_cikar(resim_bytelari)
        
        if "OCR Okuma Hatası" in okunan_metin:
             raise HTTPException(status_code=500, detail=f"OCR Hata: {okunan_metin}")
             
        # Adım 2: Çıkan metni analiz et ve risk sonucunu dön (Analiz Engine)
        risk_sonucu = alerji_analiz_motoru.metni_analiz_et(okunan_metin)
        return risk_sonucu
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Beklenmeyen Analiz Hatası: {str(e)}")

# ---------------------------------------------
# SYNC-MED (AİLE İLAÇ TAKİBİ VE ONAY SİSTEMİ)
# ---------------------------------------------
class IlacOnayistegi(BaseModel):
    ilac_id: int
    kullanici_id: int
    refakatci_token: Optional[str] = None # Gecikme anında refakatçiye (veli) bildirim gitmesi için

@app.get("/ilac-takip/{kullanici_id}", response_model=List[dict])
def ilaclari_getir(kullanici_id: int, db: Session = Depends(get_db)):
    """
    Belirli bir kullanıcının (veya aile üyesinin) ilaç listesini getirir.
    """
    ilaclar = db.query(models.Ilac).filter(models.Ilac.kullanici_id == kullanici_id).all()
    return [
        {
            "id": i.id,
            "isim": i.ilac_adi,
            "saat": i.alinacak_saat,
            "talimat": i.talimat,
            "alindi_mi": i.alindi_mi,
            "olcek": i.doz,
            # Mock veriler (Veritabanında şimdilik olmayanlar)
            "gecikti_mi": False, 
            "kalan_kutu": 10
        } for i in ilaclar
    ]

@app.post("/ilac-takip/onayla")
def ilac_onayla(veri: IlacOnayistegi, db: Session = Depends(get_db)):
    """
    Kullanıcı ilacını içtiğinde veritabanında durumu güncellenir.
    Ortak Takip için eşlerin uygulamasında da 'Verildi' olarak senkronize olur.
    """
    ilac = db.query(models.Ilac).filter(models.Ilac.id == veri.ilac_id).first()
    if not ilac:
        raise HTTPException(status_code=404, detail="İlaç bulunamadı.")
        
    ilac.alindi_mi = True
    db.commit()
    
    return {"durum": "basarili", "mesaj": f"{ilac.ilac_adi} başarıyla alındı olarak işaretlendi."}

@app.post("/ilac-takip/akilli-ekle")
async def akilli_ilac_ekle(kullanici_id: int, dosya: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Kutunun fotoğrafından ilaç bilgilerini çıkartır ve kaydeder.
    """
    resim_bytelari = await dosya.read()
    okunan_metin = ocr_motoru.resimden_metin_cikar(resim_bytelari)
    
    # Mock Parsing (Gelişmiş NLP yerine anahtar kelime avı)
    # Gerçek senaryoda GPT-4o-mini gibi bir modelle bu metin JSON'a çevrilir.
    ilac_adi = "Bilinmeyen İlaç"
    if "parol" in okunan_metin.lower(): ilac_adi = "Parol"
    elif "aspirin" in okunan_metin.lower(): ilac_adi = "Aspirin"
    elif "advil" in okunan_metin.lower(): ilac_adi = "Advil"

    yeni_ilac = models.Ilac(
        kullanici_id=kullanici_id,
        ilac_adi=ilac_adi,
        doz="1 Tablet",
        alinacak_saat="12:00",
        talimat="Tok Karnına",
        alindi_mi=False
    )
    db.add(yeni_ilac)
    db.commit()
    db.refresh(yeni_ilac)
    
    return {"durum": "basarili", "ilac": yeni_ilac, "ham_metin": okunan_metin}

@app.post("/ilac-takip/gecikme-uyarisi")
def gecikme_uyarisi_tetikle(hasta_adi: str, ilac_adi: str, refakatci_token: str, arka_plan_gorevleri: BackgroundTasks):
    """
    Kullanıcı ilacı zamanında 'Onayla' butonuna basmadığında çalışır.
    Refakatçiye Anlık Firebase Push Notification atar.
    """
    arka_plan_gorevleri.add_task(
        ilac_takip_motoru.gecikme_uyarisi_ver, 
        refakatci_fcm_token=refakatci_token, 
        hasta_adi=hasta_adi, 
        ilac_adi=ilac_adi
    )
    return {"durum": "uyari_siraya_alindi", "mesaj": "Gecikme analizi başlatıldı, refakatçiye bildirim iletiliyor."}

# ---------------------------------------------
# HEALTH-NAV (ACİL DURUM & NAVİGASYON)
# ---------------------------------------------
@app.get("/navigasyon/eczaneler")
def eczaneleri_getir(enlem: float, boylam: float):
    """
    Kullanıcı konumuna en yakın NÖBETÇİ eczaneleri döndürür.
    """
    eczaneler = navigasyon_motoru.yakin_eczaneleri_getir(enlem, boylam)
    return {"sayi": len(eczaneler), "veri": eczaneler}

@app.get("/navigasyon/hastaneler")
def hastaneleri_getir(enlem: float, boylam: float, filtre_turu: str = "Tümü"):
    """
    Konum bazlı hastaneleri filtreleyerek (Örn: Çocuk Acil) listeler.
    """
    hastaneler = navigasyon_motoru.yakin_hastaneleri_getir(enlem, boylam, filtre_turu)
    return {"sayi": len(hastaneler), "uygulanan_filtre": filtre_turu, "veri": hastaneler}

# ---------------------------------------------
# LIFE-COACH (WELLNESS & DOĞAL SAĞLIK)
# ---------------------------------------------
@app.get("/yasam-kocu/recete")
def dogal_recete_getir(semptom: str):
    """
    Belirtilen semptom (uykusuzluk, bağışıklık) için bitkisel destek (DoğaReçetem) getirir.
    """
    receteler = yasam_kocu_motoru.recete_getir(semptom)
    if not receteler:
         return {"mesaj": "Bu şikayete özel doğal bir reçete bulunamadı."}
    return {"semptom": semptom, "tavsiyeler": receteler}

class EtkilesimKontrolistegi(BaseModel):
    bitki_veya_takviye: str
    aktif_ilaclar: List[str]

@app.post("/yasam-kocu/etkilesim-kontrol")
def bitki_ilac_etkilesim_kontrolu(veri: EtkilesimKontrolistegi):
    """
    Kullanıcının almayı düşündüğü bitki/Gıda takviyesi ile kullandığı ilaçlar arasındaki 
    çapraz reaksiyon riskini ölçer.
    """
    sonuc = yasam_kocu_motoru.etkilesim_kontrol_et(veri.bitki_veya_takviye, veri.aktif_ilaclar)
    return sonuc

# ---------------------------------------------
# FORMDA KAL (DİYET & KALORİ TAKİBİ)
# ---------------------------------------------
class YemekKayitistegi(BaseModel):
    kullanici_id: int
    yemek_adi: str
    kalori: int
    protein: Optional[int] = 0
    karbonhidrat: Optional[int] = 0
    yag: Optional[int] = 0

@app.get("/diyet/ozet/{kullanici_id}")
def diyet_ozeti_getir(kullanici_id: int, db: Session = Depends(get_db)):
    """
    Kullanıcının bugünkü toplam kalori ve makro besin verilerini döner.
    """
    import datetime
    bugun = datetime.date.today()
    kayitlar = db.query(models.DiyetKaydi).filter(
        models.DiyetKaydi.kullanici_id == kullanici_id,
        func.date(models.DiyetKaydi.tarih) == bugun
    ).all()
    
    toplam_kalori = sum(k.kalori for k in kayitlar)
    toplam_protein = sum(k.protein for k in kayitlar)
    toplam_karbonhidrat = sum(k.karbonhidrat for k in kayitlar)
    toplam_yag = sum(k.yag for k in kayitlar)
    
    return {
        "toplam_kalori": toplam_kalori,
        "toplam_protein": toplam_protein,
        "toplam_karbonhidrat": toplam_karbonhidrat,
        "toplam_yag": toplam_yag,
        "kayit_sayisi": len(kayitlar)
    }

@app.post("/diyet/yemek-ekle")
def yemek_ekle(veri: YemekKayitistegi, db: Session = Depends(get_db)):
    """
    Yeni bir yemek veya kaçamak kaydı oluşturur.
    """
    yeni_kayit = models.DiyetKaydi(
        kullanici_id=veri.kullanici_id,
        yemek_adi=veri.yemek_adi,
        kalori=veri.kalori,
        protein=veri.protein,
        karbonhidrat=veri.karbonhidrat,
        yag=veri.yag
    )
    db.add(yeni_kayit)
    db.commit()
    db.refresh(yeni_kayit)
    return {"durum": "basarili", "mesaj": f"{veri.yemek_adi} kaydedildi.", "id": yeni_kayit.id}

@app.post("/diyet/foto-analiz")
async def yemek_foto_analiz(dosya: UploadFile = File(...)):
    """
    Yemek fotoğrafını alır, OCR ile varsa menüdeki ismi okur 
    veya AI ile yemeği tahmin ederek kalori değerlerini döner.
    """
    resim_bytelari = await dosya.read()
    okunan_metin = ocr_motoru.resimden_metin_cikar(resim_bytelari)
    
    analiz_sonucu = diyet_motoru.yemek_analiz_et(okunan_metin)
    return {
        "durum": "basarili",
        "tahmin edilen_yemek": analiz_sonucu["yemek_adi"],
        "degerler": analiz_sonucu["analiz"],
        "tavsiye": analiz_sonucu["tavsiye"],
        "ham_metin": okunan_metin
    }

# ---------------------------------------------
# AİLE AĞI (KONUM TAKİBİ & SOS)
# ---------------------------------------------
class KonumGuncelleme(BaseModel):
    kullanici_id: int
    enlem: str
    boylam: str

class SOSGonderimi(BaseModel):
    kullanici_id: int
    mesaj: str
    enlem: str
    boylam: str

@app.post("/aile/konum-guncelle")
def konum_guncelle(veri: KonumGuncelleme, db: Session = Depends(get_db)):
    kullanici = db.query(models.Kullanici).filter(models.Kullanici.id == veri.kullanici_id).first()
    if not kullanici: return {"hata": "Kullanici bulunamadi"}
    
    kullanici.enlem = veri.enlem
    kullanici.boylam = veri.boylam
    db.commit()
    return {"durum": "basarili"}

@app.get("/aile/uyeler/{aile_id}")
def aile_uyelerini_getir(aile_id: str, db: Session = Depends(get_db)):
    uyeler = db.query(models.Kullanici).filter(models.Kullanici.aile_id == aile_id).all()
    return [
        {
            "id": u.id,
            "ad_soyad": u.ad_soyad,
            "rol": u.rol,
            "enlem": u.enlem,
            "boylam": u.boylam,
            "son_gorulme": u.son_gorulme
        } for u in uyeler
    ]

@app.post("/aile/sos")
def sos_gonder(veri: SOSGonderimi, db: Session = Depends(get_db)):
    sos = models.SOSLog(
        kullanici_id=veri.kullanici_id,
        mesaj=veri.mesaj,
        enlem=veri.enlem,
        boylam=veri.boylam
    )
    db.add(sos)
    db.commit()
    
    # Gerçek senaryoda burada tüm aile üyelerine PUSH NOTIFICATION gider.
    return {"durum": "SOS_YAYINLANDI", "mesaj": "Tüm aile üyelerine acil durum bildirimi iletildi!"}
