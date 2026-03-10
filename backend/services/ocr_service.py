import pytesseract
from PIL import Image
import io
import os

class OcrServisi:
    def __init__(self):
        # Tesseract OCR yüklü değilse, bilgisayardaki yolunu burada belirtmek gerekebilir.
        # Genellikle Windows için: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Windows Tesseract yolunu belirtiyoruz (Yüklü değilse hata vermesin diye varsayılan bir ayar yapıyoruz)
        # Eğer bu hata verirse, kullanıcının bilgisayarına Tesseract kurması gerekecektir.
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # Yerel tessdata klasörümüzü belirtiyoruz (tur.traineddata burada olduğu için)
        self.tessdata_path = os.path.dirname(os.path.abspath(__file__)) # services klasörü
        self.tessdata_path = os.path.dirname(self.tessdata_path) # backend klasörü

    def resimden_metin_cikar(self, resim_bytelari: bytes) -> str:
        """
        Gelen görsel bytelarından metni çıkartır.
        """
        try:
            # Gelen byte verisini bir Pillow nesnesine (görsel) çevir
            resim = Image.open(io.BytesIO(resim_bytelari))
            
            # Tesseract OCR ile görselden metni (Türkçe ve İngilizce) oku
            # Dil için Tesseract'ın tr ve eng datalarına ihtiyacı var
            config = f'--tessdata-dir "{self.tessdata_path}"'
            metin = pytesseract.image_to_string(resim, lang='tur+eng', config=config)
            return metin.strip()
        except Exception as e:
            # Tesseract kurulu olmadığında veya resim bozuk olduğunda fırlatılır
            return f"OCR Okuma Hatası: {str(e)}"

# OCR Servisini başlat
ocr_motoru = OcrServisi()
