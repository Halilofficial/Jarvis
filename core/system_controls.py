import datetime
import platform
import psutil

class SystemControls:
    def __init__(self):
        pass

    def get_current_time(self):
        """Sistemin mevcut saatini döndürür."""
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")

    def get_current_date(self):
        """Sistemin mevcut tarihini döndürür."""
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")
2
    def get_battery_status(self):
        """Pil durumunu (yüzde, şarj durumu) döndürür."""
        battery = psutil.sensors_battery()
        if battery:
            plugged = "takılı" if battery.power_plugged else "takılı değil"
            return f"Pil seviyesi: %{battery.percent}, Şarj durumu: {plugged}"
        return "Pil durumu bilgisi alınamıyor."

    def toggle_lights(self, state): # Bu fonksiyon örnek amaçlıdır, gerçek bir donanım entegrasyonu gerektirir.
        """Işıkları açar veya kapatır. (Örnek fonksiyon)"""
        if state == "aç":
            return "Işıklar açıldı (simüle edildi)."
        elif state == "kapat":
            return "Işıklar kapatıldı (simüle edildi)."
        else:
            return "Geçersiz ışık durumu. 'aç' veya 'kapat' kullanın."

    def get_system_info(self):
        """Sistem hakkında genel bilgi döndürür."""
        info = {
            "İşletim Sistemi": platform.system(),
            "İşletim Sistemi Sürümü": platform.version(),
            "Mimari": platform.machine(),
            "İşlemci": platform.processor(),
            "RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
        }
        return "\n".join([f"{k}: {v}" for k, v in info.items()])