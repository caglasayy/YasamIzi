from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Kullanici(Base):
    __tablename__ = "kullanicilar"

    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String, unique=True, index=True) # Firebase'den gelecek eşsiz kimlik
    ad_soyad = Column(String)
    eposta = Column(String, unique=True, index=True)
    rol = Column(String, default="ebeveyn") # ebeveyn, cocuk, yasli vb.
    olusturma_tarihi = Column(DateTime(timezone=True), server_default=func.now())

class Ilac(Base):
    __tablename__ = "ilaclar"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id"))
    ilac_adi = Column(String, index=True)
    doz = Column(String)
    alinacak_saat = Column(String) # Örn: '08:00', '20:00'
    talimat = Column(String) # Aç karnına / Tok karnına
    alindi_mi = Column(Boolean, default=False)
