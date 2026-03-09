from typing import List, Dict

class YasamKocuServisi:
    def __init__(self):
        # Örnek İlaç-Bitki Etkileşim Veritabanı
        self.etkilesimler = {
            "sarı kantaron": ["antidepresan", "kan sulandırıcı", "doğum kontrol hapı"],
            "ginseng": ["kan sulandırıcı", "diyabet ilacı"],
            "greyfurt": ["kolesterol ilacı", "tansiyon ilacı"],
            "zencefil": ["kan sulandırıcı"],
            "sarımsak ekstresi": ["kan sulandırıcı"]
        }
        
        # Örnek Doğa Reçeteleri
        self.dogal_receteler = {
            "uykusuzluk": [
                {"isim": "Papatya Çayı", "aciklama": "Uyumadan 1 saat önce hafif demlenmiş papatya çayı rahatlatabilir."},
                {"isim": "Melisa (Oğul Otu)", "aciklama": "Sinirleri yatıştırır ve uykuya dalmayı kolaylaştırır."}
            ],
            "bağışıklık": [
                {"isim": "Zencefil & Bal & Limon", "aciklama": "Boğazı yumuşatır ve bağışıklığı destekler."},
                {"isim": "Ekinezya", "aciklama": "Soğuk algınlığında, hastalığın ilk günlerinde destekleyicidir."}
            ],
            "baş ağrısı": [
                {"isim": "Nane Yağı", "aciklama": "Şakaklara masaj yaparak uygulanması gerilimi azaltabilir."},
                {"isim": "Su Tüketimi", "aciklama": "Ağrıların büyük çoğunluğu susuzluk (dehidrasyon) kaynaklıdır. En az 2 bardak su içiniz."}
            ]
        }

    def etkilesim_kontrol_et(self, bitki: str, aktif_ilaclar: List[str]) -> Dict:
        """
        Kullanıcının kullanmak istediği doğal takviye/bitki ile 
        halihazırda kullandığı ilaçlar arasında tehlikeli bir etkileşim var mı kontrol eder.
        """
        bitki_kucuk = bitki.lower().strip()
        cakismalar = []
        
        if bitki_kucuk in self.etkilesimler:
            riskli_ilac_gruplari = self.etkilesimler[bitki_kucuk]
            for ilac in aktif_ilaclar:
                ilac_kucuk = ilac.lower()
                for riskli_grup in riskli_ilac_gruplari:
                    if riskli_grup in ilac_kucuk or ilac_kucuk in riskli_grup:
                         cakismalar.append(ilac)
                         
        if cakismalar:
            return {
                "guvenli_mi": False, 
                "mesaj": f"DİKKAT! '{bitki}' kullanımı, şu an aldığınız şu ilaç(lar) ile etkileşime girebilir: {', '.join(cakismalar)}. Mutlaka doktorunuza danışınız."
            }
        return {"guvenli_mi": True, "mesaj": f"'{bitki}' için bilinen bir riskli ilaç etkileşimi sistemimizde bulunamadı."}

    def recete_getir(self, semptom: str) -> List[Dict]:
        """
        Belirtilen şikayete (uykusuzluk, bağışıklık vb.) iyi gelebilecek doğal önerileri (DoğaReçetem) döner.
        """
        return self.dogal_receteler.get(semptom.lower().strip(), [])

yasam_kocu_motoru = YasamKocuServisi()
