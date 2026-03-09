import firebase_admin
from firebase_admin import messaging

class IlacTakipServisi:
    @staticmethod
    def hatirlatici_gonder(kullanici_fcm_token: str, ilac_adi: str, saat: str):
        try:
            mesaj = messaging.Message(
                notification=messaging.Notification(
                    title=f"İlaç Vakti: {ilac_adi}",
                    body=f"Saat {saat} ilacınızı alma vaktiniz geldi. Lütfen aldıktan sonra onaylayın.",
                ),
                token=kullanici_fcm_token,
            )
            cevap = messaging.send(mesaj)
            return f"Hatırlatıcı başarıyla gönderildi: {cevap}"
        except Exception as e:
            return f"Bildirim Hatası: {str(e)}"

    @staticmethod
    def gecikme_uyarisi_ver(refakatci_fcm_token: str, hasta_adi: str, ilac_adi: str):
        try:
            mesaj = messaging.Message(
                notification=messaging.Notification(
                    title="DİKKAT! Gecikmiş İlaç Bildirimi",
                    body=f"{hasta_adi}, '{ilac_adi}' isimli ilacını zamanında onaylamadı. Lütfen kontrol ediniz.",
                ),
                token=refakatci_fcm_token,
            )
            cevap = messaging.send(mesaj)
            return f"Gecikme uyarısı gönderildi: {cevap}"
        except Exception as e:
            return f"Bildirim Hatası: {str(e)}"

ilac_takip_motoru = IlacTakipServisi()
