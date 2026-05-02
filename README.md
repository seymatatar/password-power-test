# 🔐 Password Power & Risk Analyzer

Bu proje, şifrelerin güvenliğini siber güvenlik perspektifiyle analiz eden bir Python uygulamasıdır. Sadece şifre karmaşıklığını ölçmekle kalmaz, aynı zamanda bir saldırganın bu şifreyi **Brute Force (Kaba Kuvvet)** yöntemiyle ne kadar sürede kırabileceğini matematiksel olarak hesaplar.

## ✨ Öne Çıkan Özellikler
- **Kapsamlı Analiz:** Büyük/küçük harf, rakam ve özel karakter varlığını denetler.
- **Profesyonel Altyapı:** Özel karakter tespiti için Python'ın standart `string.punctuation` kütüphanesini kullanır.
- **Dinamik Süre Tahmini:** Şifrenin karakter havuzu genişliğine göre saniye, dakika, gün veya yıl bazlı insancıl sonuçlar üretir.
- **Güvenli Döngü:** Kullanıcı `q` tuşuna basana kadar kesintisiz çalışır ve her girişi sıfırdan analiz eder.
- **🔐 Gizlilik Taahhüdü:** Bu uygulama etik sınırlar çerçevesinde geliştirilmiştir; test edilen şifreler hiçbir şekilde kaydedilmez veya paylaşılmaz.

## 🧮 Teknik Detaylar
Uygulama, saniyede ortalama 1.000.000.000 (1 Milyar) deneme yapabilen modern bir saldırgan donanımını simüle eder. Hesaplama şu formüle dayanır:$$ \text{Olasılık} = (\text{Karakter Havuzu})^{\text{Şifre Uzunluğu}} $$

## 🚀 Çalıştırma 
Sisteminizde Python 3 yüklü olması yeterlidir:
```bash
python password_power_test.py

⚖️ Lisans
Bu proje MIT lisansı altında sunulmaktadır.
