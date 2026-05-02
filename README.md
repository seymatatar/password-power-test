# 🔐 Password Power & Risk Analyzer

<p align="center">
  <a href="#-english">English</a> | 
  <a href="#-turkish">Turkish</a>
</p>

---

## 🇺🇸 English

This project is a Python application that analyzes password security from a cybersecurity perspective. It doesn't just measure password complexity; it also mathematically calculates how long it would take for an attacker to crack the password using **Brute Force** methods.

### ✨ Key Features
- **Comprehensive Analysis:** Checks for uppercase, lowercase, numbers, and special characters.
- **Professional Infrastructure:** Uses Python's standard `string.punctuation` library for precise special character detection.
- **Dynamic Time Estimation:** Produces human-readable results (seconds, minutes, days, or years) based on the password's character pool size.
- **Secure Loop:** Runs continuously until the user presses `q`, analyzing each entry from scratch.
- **🔐 Privacy Commitment:** Developed within ethical boundaries; tested passwords are never recorded, logged, or shared.

### 🧮 Technical Details
The application simulates modern attacker hardware capable of an average of **1,000,000,000 (1 Billion)** attempts per second. The calculation is based on this formula:

$$ \text{Probability} = (\text{Character Pool})^{\text{Password Length}} $$

### 🚀 Usage
Python 3 is required to run this application.
```bash
python password_power_test.py
```

### ⚖️ License
This project is provided under the MIT License.



# 🔐 Password Power & Risk Analyzer

## 🇺🇸 Turkish

Bu proje, şifrelerin güvenliğini siber güvenlik perspektifiyle analiz eden bir Python uygulamasıdır. Sadece şifre karmaşıklığını ölçmekle kalmaz, aynı zamanda bir saldırganın bu şifreyi **Brute Force (Kaba Kuvvet)** yöntemiyle ne kadar sürede kırabileceğini matematiksel olarak hesaplar.

### ✨ Öne Çıkan Özellikler
- **Kapsamlı Analiz:** Büyük/küçük harf, rakam ve özel karakter varlığını denetler.
- **Profesyonel Altyapı:** Özel karakter tespiti için Python'ın standart `string.punctuation` kütüphanesini kullanır.
- **Dinamik Süre Tahmini:** Şifrenin karakter havuzu genişliğine göre saniye, dakika, gün veya yıl bazlı insancıl sonuçlar üretir.
- **Güvenli Döngü:** Kullanıcı `q` tuşuna basana kadar kesintisiz çalışır ve her girişi sıfırdan analiz eder.
- **🔐 Gizlilik Taahhüdü:** Bu uygulama etik sınırlar çerçevesinde geliştirilmiştir; test edilen şifreler hiçbir şekilde kaydedilmez veya paylaşılmaz.

### 🧮 Teknik Detaylar
Uygulama, saniyede ortalama **1.000.000.000 (1 Milyar)** deneme yapabilen modern bir saldırgan donanımını simüle eder. Hesaplama şu formüle dayanır:

$$ \text{Olasılık} = (\text{Karakter Havuzu})^{\text{Şifre Uzunluğu}} $$

### 🚀 Çalıştırma
Sisteminizde Python 3 yüklü olması yeterlidir.
```bash
python password_power_test.py
```
### ⚖️ Lisans
Bu proje MIT lisansı altında sunulmaktadır.
