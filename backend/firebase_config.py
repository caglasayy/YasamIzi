import firebase_admin
from firebase_admin import credentials
import os
from dotenv import load_dotenv

load_dotenv()

# Firebase admin SDK json dosyasının yolu. 
# İleride Firebase projesi oluşturduğunuzda bu json dosyasını eklemeniz gerekecek.
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase-adminsdk.json")

def initialize_firebase():
    if not firebase_admin._apps:
        try:
            if os.path.exists(FIREBASE_CREDENTIALS_PATH):
                cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
                firebase_admin.initialize_app(cred)
                print("Firebase başarıyla başlatıldı.")
            else:
                print("UYARI: Firebase Credentials JSON dosyası bulunamadı. Firebase başlatılmadı.")
        except Exception as e:
            print(f"Firebase başlatılırken bir hata oluştu: {e}")
