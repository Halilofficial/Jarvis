import os

# OpenRouter API Yapılandırması
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "YOUR_OPENROUTER_API_KEY")
OPENROUTER_MODEL = "openrouter/auto"

# Diğer Yapılandırmalar
APP_TITLE = "Jarvis AI Asistanı"
APP_VERSION = "1.0.0"

# Sesli Sohbet Yapılandırması
TTS_LANG = "tr"
STT_LANG = "tr-TR"

# Dosya Kayıt Dizini
GENERATED_FILES_DIR = "./generated_files"
