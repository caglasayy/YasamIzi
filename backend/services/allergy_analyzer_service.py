from pydantic import BaseModel
from typing import List

class AlerjiRiski(BaseModel):
    risk_seviyesi: str  # KIRMIZI, SARI, YESIL
    tespit_edilen_alerjenler: List[str]
    aciklama: str

class AlerjiAnalizServisi:
    def __init__(self):
        # Örnek Alerjen Veri Tabanı
        self.kirmizi_alerjenler = ["fıstık", "yer fıstığı", "penisilin", "süt", "laktoz"]
        self.sari_alerjenler = ["glüten", "soya", "maya", "esansiyel yağ"]

    def metni_analiz_et(self, okunan_metin: str, kullanici_alerjenleri: List[str] = None) -> AlerjiRiski:
        metin_kucuk = okunan_metin.lower()
        
        # Eğer kullanıcının özel bir alerjen listesi varsa onu kullan.
        hedef_alerjenler = kullanici_alerjenleri if kullanici_alerjenleri else self.kirmizi_alerjenler
        
        bulunan_kirmizi = [alerjen for alerjen in hedef_alerjenler if alerjen.lower() in metin_kucuk]
        bulunan_sari = [alerjen for alerjen in self.sari_alerjenler if alerjen.lower() in metin_kucuk]

        if bulunan_kirmizi:
            return AlerjiRiski(
                risk_seviyesi="KIRMIZI",
                tespit_edilen_alerjenler=bulunan_kirmizi,
                aciklama="DİKKAT! Bu ürün/ilaç doğrudan alerjik reaksiyona sebep olabilecek maddeler içeriyor."
            )
        elif bulunan_sari:
            return AlerjiRiski(
                risk_seviyesi="SARI",
                tespit_edilen_alerjenler=bulunan_sari,
                aciklama="UYARI: Bu ürün/ilaç çapraz reaksiyon veya eser miktarda hassasiyet yaratabilecek maddeler içerebilir."
            )
        else:
            return AlerjiRiski(
                risk_seviyesi="YESIL",
                tespit_edilen_alerjenler=[],
                aciklama="GÜVENLİ: Ürün içeriğinde bilinen bir alerjen maddesine rastlanmadı."
            )

alerji_analiz_motoru = AlerjiAnalizServisi()
