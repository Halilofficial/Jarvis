import requests
import json
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL

class AIManager:
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.model = OPENROUTER_MODEL
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_completion(self, messages):
        payload = {
            "model": self.model,
            "messages": messages
        }
        try:
            response = requests.post(self.base_url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()  # HTTP hatalarını kontrol et
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API isteği hatası: {e}")
            return {"error": str(e)}

    def chat(self, user_message, history=None):
        if history is None:
            history = []

        messages = history + [{"role": "user", "content": user_message}]
        response = self.get_completion(messages)

        if "choices" in response and response["choices"]:
            ai_response = response["choices"][0]["message"]["content"]
            history.append({"role": "user", "content": user_message})
            history.append({"role": "assistant", "content": ai_response})
            return ai_response, history
        elif "error" in response:
            return f"Hata: {response['error']}", history
        else:
            return "Üzgünüm, bir yanıt alamadım.", history

