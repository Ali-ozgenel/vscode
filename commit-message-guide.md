# 🧩 Commit Mesajı Rehberi

## 🪶 Temel format
```
<type>: <kısa açıklama>
```

## 🧠 Uzun açıklama eklemek istersen
```
<type>: <kısa açıklama>

<isteğe bağlı detaylı açıklama — ne, neden, nasıl değişti>
```

---

## 🔹 Commit Türleri (type)

| Tür (type) | Açıklama | Örnek |
|-------------|-----------|--------|
| **feat** | Yeni bir özellik eklendi | `feat: add bank account system` |
| **fix** | Hata düzeltildi | `fix: correct withdrawal balance calculation` |
| **docs** | Yalnızca dokümantasyon değişti | `docs: update README with setup instructions` |
| **style** | Biçim/düzen değişiklikleri (kod yapısı değil) | `style: format code and fix indentation` |
| **refactor** | Kod yapısı değişti ama işlev aynı | `refactor: simplify transaction logic` |
| **test** | Test dosyaları eklendi/değişti | `test: add deposit function tests` |
| **chore** | Küçük bakım, yapı veya bağımlılık değişikliği | `chore: update .gitignore for pycache` |
| **perf** | Performans iyileştirmesi | `perf: improve transaction lookup speed` |

---

## 🔸 Kısa + Uzun mesaj örneği
```bash
git commit -m "feat: create bank account system" -m "Added deposit and withdraw functions to handle basic transactions. This lays the foundation for future interest calculation features."
```

---

## ✍️ Kullanım şablonu
```bash
git commit -m "<type>: <kısa açıklama>" -m "<isteğe bağlı detaylı açıklama>"
```

### 💡 Örnek
```bash
git commit -m "feat: add number guessing game" -m "User guesses a random number between 1 and 100. Includes basic input validation."
```

---

## 🎯 İpuçları
- Kısa açıklama 50 karakteri geçmesin.  
- İlk harf küçük, sonuna nokta koyma.  
- Türkçe veya İngilizce olabilir ama projede tek dilde tutarlı ol.  
- Gereksiz uzun yazma — ne yaptığını kısaca anlat.
