import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Çevresel değişkenleri yükle (.env dosyasından)
load_dotenv()

# Şimdilik bilgisayarınızda PostgreSQL kurulu olmadığı için, testi kolaylaştırmak adına
# geçici olarak yerel bir SQLite veritabanı (dosya tabanlı) kullanıyoruz.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./yasamizi.db")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Veritabanı Session (oturum) yönetimi için bağımlılık fonksiyonu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
