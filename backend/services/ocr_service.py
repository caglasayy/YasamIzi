import pytesseract
from PIL import Image
import io

class OcrServisi:
    def __init__(self):
        # Tesseract OCR yüklü değilse, bilgisayardaki yolunu burada belirtmek gerekebilir.
        # Genellikle Windows için: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Windows Tesseract yolunu belirtiyoruz (Yüklü değilse hata vermesin diye varsayılan bir ayar yapıyoruz)
        # Eğer bu hata verirse, kullanıcının bilgisayarına Tesseract kurması gerekecektir.
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def resimden_metin_cikar(self, resim_bytelari: bytes) -> str:
        """
        Gelen görsel bytelarından metni çıkartır.
        """
        try:
            # Gelen byte verisini bir Pillow nesnesine (görsel) çevir
            resim = Image.open(io.BytesIO(resim_bytelari))
            
            # Tesseract OCR ile görselden metni (Türkçe ve İngilizce) oku
            # Dil için Tesseract'ın tr ve eng datalarına ihtiyacı var
            metin = pytesseract.image_to_string(resim, lang='tur+eng')
            return metin.strip()
        except Exception as e:
            # Tesseract kurulu olmadığında veya resim bozuk olduğunda fırlatılır
            return f"OCR Okuma Hatası: {str(e)}"

# OCR Servisini başlat
ocr_motoru = OcrServisi()
