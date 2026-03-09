from typing import List, Dict

class NavigasyonServisi:
    def __init__(self):
        # Gerçek uygulamada Google Maps API kullanılacak. 
        # (Örn: googlemaps.Client(key='YOUR_API_KEY'))
        # Şimdilik örnek veri dönen bir simülasyon kuruyoruz.
        pass

    def yakin_eczaneleri_getir(self, enlem: float, boylam: float) -> List[Dict]:
        """
        Kullanıcının koordinatlarına (Enlem, Boylam) en yakın nöbetçi eczaneleri döndürür.
        """
        # Burada ileride Google Places API veya Nöbetçi Eczane API'sine HTTP isteği atılacak.
        return [
            {
                "ad": "Şifa Eczanesi",
                "mesafe": "0.4 km",
                "nobetci_mi": True,
                "adres": "Atatürk Caddesi No:45",
                "enlem": enlem + 0.005,
                "boylam": boylam + 0.005
            },
            {
                "ad": "Merkez Eczane",
                "mesafe": "1.2 km",
                "nobetci_mi": True,
                "adres": "Cumhuriyet Meydanı",
                "enlem": enlem - 0.010,
                "boylam": boylam + 0.015
            }
        ]

    def yakin_hastaneleri_getir(self, enlem: float, boylam: float, filtre_turu: str = "Tümü") -> List[Dict]:
        """
        Filtreye (Devlet, Özel, Çocuk Acil) göre en yakın hastaneleri listeler.
        """
        hastaneler = [
            {
                "ad": "Şehir Devlet Hastanesi",
                "tur": "Devlet",
                "cocuk_acil_var_mi": True,
                "mesafe": "2.1 km",
                "enlem": enlem + 0.02,
                "boylam": boylam - 0.01
            },
            {
                "ad": "Medikal Acil Tıp Merkezi",
                "tur": "Özel",
                "cocuk_acil_var_mi": False,
                "mesafe": "3.5 km",
                "enlem": enlem - 0.03,
                "boylam": boylam - 0.02
            }
        ]
        
        if filtre_turu == "Çocuk Acil":
            return [h for h in hastaneler if h["cocuk_acil_var_mi"]]
        elif filtre_turu != "Tümü":
            return [h for h in hastaneler if h["tur"] == filtre_turu]
            
        return hastaneler

navigasyon_motoru = NavigasyonServisi()
