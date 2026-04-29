import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import pygame
from config import TTS_LANG, STT_LANG

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.recognizer = sr.Recognizer()

    def text_to_speech(self, text):
        """Metni sese dönüştürür ve çalar."""
        try:
            tts = gTTS(text=text, lang=TTS_LANG)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                temp_filename = fp.name
                tts.save(temp_filename)
            
            pygame.mixer.music.load(temp_filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            os.remove(temp_filename)
        except Exception as e:
            print(f"TTS Hatası: {e}")

    def speech_to_text(self):
        """Mikrofondan ses alır ve metne dönüştürür."""
        with sr.Microphone() as source:
            print("Dinleniyor...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            
            try:
                text = self.recognizer.recognize_google(audio, language=STT_LANG)
                print(f"Anlaşılan: {text}")
                return text
            except sr.UnknownValueError:
                print("Ses anlaşılamadı.")
                return None
            except sr.RequestException as e:
                print(f"STT Servis Hatası: {e}")
                return None