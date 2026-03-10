import random
from typing import Dict

class DiyetServisi:
    def __init__(self):
        # Örnek yemek veritabanı (İleride AI Vision ile genişletilebilir)
        self.yemek_veritabani = {
            "pizza": {"kalori": 280, "protein": 12, "karbonhidrat": 36, "yag": 10},
            "hamburger": {"kalori": 550, "protein": 25, "karbonhidrat": 45, "yag": 28},
            "salata": {"kalori": 120, "protein": 4, "karbonhidrat": 8, "yag": 9},
            "makarna": {"kalori": 350, "protein": 11, "karbonhidrat": 68, "yag": 2},
            "kebap": {"kalori": 450, "protein": 30, "karbonhidrat": 5, "yag": 35},
            "elma": {"kalori": 52, "protein": 0, "karbonhidrat": 14, "yag": 0},
            "tavuk": {"kalori": 239, "protein": 27, "karbonhidrat": 0, "yag": 14},
        }

    def yemek_analiz_et(self, ocr_metni: str) -> Dict:
        """
        Görselden gelen metne (veya ileride doğrudan görüntüye) dayanarak 
        yemeği tanır ve besin değerlerini döner.
        """
        kucuk_metin = ocr_metni.lower()
        
        # Tanınan yemeği bul
        bulunan_yemek = "Bilinmeyen Yemek"
        besin_degerleri = {"kalori": 200, "protein": 5, "karbonhidrat": 20, "yag": 5} # Default

        for yemek, degerler in self.yemek_veritabani.items():
            if yemek in kucuk_metin:
                bulunan_yemek = yemek.capitalize()
                besin_degerleri = degerler
                break
        
        return {
            "yemek_adi": bulunan_yemek,
            "analiz": besin_degerleri,
            "tavsiye": self._tavsiye_uret(bulunan_yemek, besin_degerleri)
        }

    def _tavsiye_uret(self, yemek: str, degerler: Dict) -> str:
        if degerler["kalori"] > 400:
            return f"Bu {yemek} biraz yüksek kalorili görünüyor. Yanında bol su içmeyi ve bir sonraki öğünü hafif tutmayı unutma."
        elif degerler["protein"] > 20:
            return f"Harika! Bu {yemek} yüksek protein içeriyor, kas sağlığın için çok iyi."
        else:
            return f"{yemek} sağlıklı bir seçim gibi görünüyor, afiyet olsun!"

diyet_motoru = DiyetServisi()
