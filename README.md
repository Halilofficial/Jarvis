# Jarvis AI Uygulaması

Bu proje, OpenRouter API kullanarak yazılı ve sesli sohbet edebilen, sistem kontrolleri yapabilen ve gelişmiş bir görsel arayüze sahip bir yapay zeka asistanı olan Jarvis'i geliştirmeyi amaçlamaktadır.

## Özellikler

- **Yazılı ve Sesli Sohbet:** OpenRouter API (opentroter/free modeli) entegrasyonu ile kesintisiz iletişim.
- **Sistem Kontrolleri:** Bilgisayar saati, pil durumu gibi bilgilere erişim ve ışık kontrolü gibi temel otomasyon yetenekleri.
- **Özel Komutlar:** Kullanıcı tanımlı komutları anlama ve yürütme.
- **Dosya/Fotoğraf İşleme:** Dosya ve fotoğraf alıp gönderme yeteneği.
- **Özelleştirilebilir Sistem Promptları:** Jarvis'in davranışını yönlendirmek için özel promptlar tanımlama.
- **Modern Kullanıcı Arayüzü:** Uzay siyahı teması ve ses şiddetine göre titreşen dairesel parçacık animasyonu.

## Proje Yapısı

```
jarvis_app/
├── README.md
├── SKILL.md
├── requirements.txt
├── main.py
├── config.py
├── ui/
│   ├── __init__.py
│   ├── main_window.py
│   └── assets/
│       └── ... (arayüz varlıkları)
├── core/
│   ├── __init__.py
│   ├── ai_manager.py
│   ├── system_controls.py
│   └── audio_manager.py
└── utils/
    ├── __init__.py
    └── file_handler.py
```

## Bağımlılıklar

- `python-dotenv`
- `requests`
- `pyaudio` (ses girişi için)
- `gTTS` (metinden sese dönüştürme için)
- `SpeechRecognition` (sesten metne dönüştürme için)
- `PyQt5` (GUI için)
- `openai` (OpenRouter API ile uyumlu bir istemci olarak kullanılabilir)
- `websocket-client` (OpenRouter API için gerekli olabilir)

## Kurulum

1. Projeyi klonlayın:
   `git clone <repo_url>`
2. Bağımlılıkları yükleyin:
   `pip install -r requirements.txt`
3. `config.py` dosyasını düzenleyerek OpenRouter API anahtarınızı ve diğer ayarları girin.
4. Uygulamayı çalıştırın:
   `python main.py`