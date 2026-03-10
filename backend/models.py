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
    aile_id = Column(String, index=True) # Aileyi birleştiren ortak ID
    enlem = Column(String, nullable=True)
    boylam = Column(String, nullable=True)
    son_gorulme = Column(DateTime(timezone=True), onupdate=func.now())
    olusturma_tarihi = Column(DateTime(timezone=True), server_default=func.now())

class SOSLog(Base):
    __tablename__ = "sos_loglari"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id"))
    mesaj = Column(String)
    enlem = Column(String)
    boylam = Column(String)
    tarih = Column(DateTime(timezone=True), server_default=func.now())

class Ilac(Base):
    __tablename__ = "ilaclar"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id"))
    ilac_adi = Column(String, index=True)
    doz = Column(String)
    alinacak_saat = Column(String) # Örn: '08:00', '20:00'
    talimat = Column(String) # Aç karnına / Tok karnına
    alindi_mi = Column(Boolean, default=False)

class DiyetKaydi(Base):
    __tablename__ = "diyet_kayitlari"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id"))
    yemek_adi = Column(String)
    kalori = Column(Integer)
    protein = Column(Integer, default=0) # Gram cinsinden
    karbonhidrat = Column(Integer, default=0)
    yag = Column(Integer, default=0)
    tarih = Column(DateTime(timezone=True), server_default=func.now())
