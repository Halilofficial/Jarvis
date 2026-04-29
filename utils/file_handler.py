import os
from config import GENERATED_FILES_DIR

def save_generated_file(filename, content):
    """Üretilen içeriği bir dosyaya kaydeder."""
    if not os.path.exists(GENERATED_FILES_DIR):
        os.makedirs(GENERATED_FILES_DIR)
    
    filepath = os.path.join(GENERATED_FILES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def list_generated_files():
    """Üretilen dosyaları listeler."""
    if not os.path.exists(GENERATED_FILES_DIR):
        return []
    return os.listdir(GENERATED_FILES_DIR)
