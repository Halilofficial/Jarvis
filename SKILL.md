# Jarvis Dosya Üretme Yeteneği

Jarvis, kullanıcıların talepleri doğrultusunda çeşitli formatlarda dosyalar üretebilir ve bu dosyaları kullanıcıya sunabilir. Bu yetenek, raporlar, kod parçacıkları, metin belgeleri veya diğer yapılandırılmış veriler gibi içeriklerin oluşturulmasını kapsar.

## Yetenek Açıklaması

Jarvis, aldığı komutları analiz ederek uygun dosya türünü ve içeriğini belirler. Örneğin, bir kullanıcı bir Python kodu yazmasını istediğinde, Jarvis bu kodu oluşturur ve `.py` uzantılı bir dosya olarak kaydeder. Benzer şekilde, bir rapor talebinde `.md` veya `.txt` formatında bir belge oluşturabilir.

## Kullanım Senaryoları

- **Kod Üretimi:** Belirli bir işlevi yerine getiren Python, JavaScript veya diğer programlama dillerinde kod dosyaları oluşturma.
- **Rapor Oluşturma:** Belirli bir konu hakkında özet veya detaylı raporlar hazırlama.
- **Metin Belgesi Oluşturma:** Notlar, listeler veya diğer serbest biçimli metin içeriklerini kaydetme.
- **Veri Dışa Aktarımı:** Analiz sonuçlarını veya yapılandırılmış verileri CSV, JSON gibi formatlarda dışa aktarma.

## Nasıl Kullanılır?

Kullanıcı, Jarvis'e dosya üretme isteğini doğal dilde iletebilir. Jarvis, isteği anladıktan sonra gerekli içeriği oluşturur ve kullanıcıya dosyanın hazır olduğunu bildirir. Kullanıcı, dosyayı indirmek veya görüntülemek için bir komut verebilir.

**Örnek Komutlar:**

- "Bana Fibonacci serisini hesaplayan bir Python kodu yaz ve `fibonacci.py` olarak kaydet."
- "Geçen haftanın satış verilerini özetleyen bir rapor oluştur ve `haftalik_satis_raporu.md` olarak kaydet."
- "Yapılacaklar listemi `todo.txt` dosyasına kaydet."

## Teknik Detaylar

Dosya üretme yeteneği, Jarvis'in `core/ai_manager.py` modülündeki dil modelinin çıktılarını işleyerek ve `utils/file_handler.py` modülünü kullanarak dosyaları yerel olarak kaydetmesiyle sağlanır. Üretilen dosyalar, kullanıcının erişebileceği bir konuma kaydedilir ve gerektiğinde kullanıcıya sunulur.

**Dosya Kaydetme Fonksiyonu (Örnek):**

```python
# utils/file_handler.py içinde bulunabilir
def save_file(filename, content, directory="./generated_files"):
    import os
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath
```

Bu skill, Jarvis'in çok yönlülüğünü artırarak kullanıcıların daha karmaşık görevleri otomatikleştirmesine olanak tanır.
