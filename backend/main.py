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
