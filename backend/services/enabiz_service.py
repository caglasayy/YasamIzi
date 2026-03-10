import random
from typing import Dict, List

class ENabizServisi:
    def __init__(self):
        # Tahlil parametreleri ve referans değerleri
        self.referans_degerleri = {
            "hba1c": {"min": 4.0, "max": 5.7, "birim": "%", "aciklama": "Diyabet Takibi"},
            "kolesterol": {"min": 0, "max": 200, "birim": "mg/dL", "aciklama": "Kolesterol (Total)"},
            "ldl": {"min": 0, "max": 130, "birim": "mg/dL", "aciklama": "Kötü Kolesterol"},
            "b12": {"min": 200, "max": 900, "birim": "pg/mL", "aciklama": "B12 Vitamini"},
            "d vitamini": {"min": 30, "max": 100, "birim": "ng/mL", "aciklama": "D Vitamini"},
            "demir": {"min": 60, "max": 170, "birim": "ug/dL", "aciklama": "Demir"},
            "ferritin": {"min": 13, "max": 150, "birim": "ng/mL", "aciklama": "Demir Deposu"},
        }

    def tahlil_analiz_et(self, metin: str) -> Dict:
        """
        OCR'dan gelen veya PDF'den ayıklanan metni analiz eder.
        """
        bulunan_sonuclar = []
        metin_kucuk = metin.lower()

        for anahtar, ref in self.referans_degerleri.items():
            if anahtar in metin_kucuk:
                # Basit bir değer yakalama mantığı (Örn: HbA1c: 5.4)
                # Gerçek projede regex ile çok daha hassas yapılmalı
                deger = self._deger_ayikla(metin_kucuk, anahtar)
                if deger:
                    durum = "normal"
                    if deger < ref["min"]: durum = "dusuk"
                    elif deger > ref["max"]: durum = "yuksek"
                    
                    bulunan_sonuclar.append({
                        "ad": ref["aciklama"],
                        "deger": f"{deger} {ref['birim']}",
                        "durum": durum,
                        "referans": f"{ref['min']} - {ref['max']}"
                    })

        # Yapay Zeka Özeti Üret
        ozet = self._ai_ozet_uret(bulunan_sonuclar)

        return {
            "sonuclar": bulunan_sonuclar,
            "ai_ozeti": ozet
        }

    def _deger_ayikla(self, metin: str, anahtar: str) -> float:
        # Simülasyon: Metin içinde anahtarı bulup yanındaki sayıyı almaya çalışır
        # Şimdilik rastgele gerçekçi bir değer döndürüyoruz (Test için)
        if anahtar == "hba1c": return round(random.uniform(4.5, 7.5), 1)
        if anahtar == "b12": return random.randint(150, 400)
        return round(random.uniform(10, 150), 1)

    def _ai_ozet_uret(self, sonuclar: List[Dict]) -> str:
        if not sonuclar:
            return "Metin içinde tanınabilir bir tahlil sonucu bulunamadı. Lütfen daha net bir görsel veya dosya yükleyin."
        
        kritik_olanlar = [s["ad"] for s in sonuclar if s["durum"] != "normal"]
        
        if not kritik_olanlar:
            return "Harika! Analiz edilen tüm değerleriniz referans aralıkları içinde görünüyor. Sağlıklı yaşam tarzınıza devam edin."
        
        return f"Analiz sonucunda {', '.join(kritik_olanlar)} değerlerinizde sapmalar görüldü. Özellikle bu alanlarda beslenmenize dikkat etmeniz veya doktorunuza danışmanız önerilir."

enabiz_motoru = ENabizServisi()
