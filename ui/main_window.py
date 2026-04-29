from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
from ui.particle_widget import ParticleWidget
from core.ai_manager import AIManager
from core.system_controls import SystemControls
from core.audio_manager import AudioManager
from utils.file_handler import save_generated_file, list_generated_files

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ai_manager = AIManager()
        self.system_controls = SystemControls()
        self.audio_manager = AudioManager()
        self.system_prompt = "Senin adın Jarvis. Bir AI asistanısın. Kibar, yardımcı ve zekisin. Sistem bilgilerine erişebilirsin (saat, pil vb.)."
        self.history = [
            {"role": "system", "content": self.system_prompt}
        ]
        self.initUI()

    def initUI(self):
        # Ana pencere ayarları
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Jarvis AI Asistanı')

        # Koyu tema uygulama
        self.applyDarkTheme()

        # Merkezi widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Parçacık animasyonu alanı
        self.particle_widget = ParticleWidget()
        self.main_layout.addWidget(self.particle_widget, alignment=Qt.AlignCenter)

        # Yazılı sohbet alanı
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("background-color: #2b2b2b; color: #e0e0e0; border: 1px solid #444; border-radius: 5px; padding: 5px;")
        self.main_layout.addWidget(self.chat_display)

        # Mesaj giriş alanı ve gönderme butonu
        self.input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText('Mesajınızı buraya yazın...')
        self.message_input.setStyleSheet("background-color: #3c3c3c; color: #e0e0e0; border: 1px solid #555; border-radius: 5px; padding: 5px;")
        self.input_layout.addWidget(self.message_input)

        self.send_button = QPushButton('Gönder')
        self.send_button.setStyleSheet("background-color: #007bff; color: white; border-radius: 5px; padding: 5px 10px;")
        self.input_layout.addWidget(self.send_button)

        self.voice_button = QPushButton('🎙️')
        self.voice_button.setStyleSheet("background-color: #28a745; color: white; border-radius: 5px; padding: 5px 10px; font-size: 18px;")
        self.input_layout.addWidget(self.voice_button)

        self.main_layout.addLayout(self.input_layout)

        # Sesli komut butonu bağlantısı
        self.voice_button.clicked.connect(self.listenVoice)

        # Bağlantılar (şimdilik sadece placeholder)
        self.send_button.clicked.connect(self.sendMessage)
        self.message_input.returnPressed.connect(self.sendMessage)

    def applyDarkTheme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30)) # Uzay Siyahı
        palette.setColor(QPalette.WindowText, QColor(240, 240, 240))
        palette.setColor(QPalette.Base, QColor(45, 45, 45))
        palette.setColor(QPalette.AlternateBase, QColor(30, 30, 30))
        palette.setColor(QPalette.ToolTipBase, QColor(240, 240, 240))
        palette.setColor(QPalette.ToolTipText, QColor(240, 240, 240))
        palette.setColor(QPalette.Text, QColor(240, 240, 240))
        palette.setColor(QPalette.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ButtonText, QColor(240, 240, 240))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        self.setPalette(palette)

    def sendMessage(self):
        message = self.message_input.text()
        if message:
            self.processMessage(message)

    def listenVoice(self):
        self.chat_display.append("<i>Jarvis dinliyor...</i>")
        text = self.audio_manager.speech_to_text()
        if text:
            self.chat_display.append(f"<b>Siz (Sesli):</b> {text}")
            self.processMessage(text)
        else:
            self.chat_display.append("<i>Jarvis sizi duyamadı.</i>")

    def processMessage(self, message):
        # Özel sistem komutlarını kontrol et
        if "saat kaç" in message.lower():
            response = f"Şu anki saat: {self.system_controls.get_current_time()}"
        elif "pil durumu" in message.lower():
            response = f"Sistem pil durumu: {self.system_controls.get_battery_status()}"
        elif "ışıkları" in message.lower():
            state = "aç" if "aç" in message.lower() else "kapat"
            response = self.system_controls.toggle_lights(state)
        elif "dosya üret" in message.lower() or "dosya oluştur" in message.lower():
            # Örnek bir dosya üretme mantığı
            content = "Bu dosya Jarvis tarafından üretilmiştir.\n\n" + message
            filename = "jarvis_output.txt"
            path = save_generated_file(filename, content)
            response = f"İsteğiniz üzerine '{filename}' dosyasını oluşturdum. Yol: {path}"
        elif "sistem promptunu değiştir" in message.lower():
            new_prompt = message.split("değiştir")[-1].strip()
            if new_prompt:
                self.system_prompt = new_prompt
                self.history = [{"role": "system", "content": self.system_prompt}]
                response = f"Sistem promptu güncellendi: {self.system_prompt}"
            else:
                response = "Lütfen yeni bir sistem promptu belirtin."
        else:
            # AI yanıtı al
            response, self.history = self.ai_manager.chat(message, self.history)
        
        self.chat_display.append(f"<b>Jarvis:</b> {response}")
        self.message_input.clear()
        
        # Yanıtı seslendir ve animasyonu tetikle
        self.particle_widget.set_volume(0.8)
        self.audio_manager.text_to_speech(response)
        self.particle_widget.set_volume(0)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())