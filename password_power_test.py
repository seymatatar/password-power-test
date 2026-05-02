import string
while True:
    print("\n" + "-"*30)
    password = input("Test etmek istediğiniz şifrenizi giriniz.(çıkış için 'q' tuşuna basın): ") #kullanıcıdan şifre alımı

    if password.lower() == "q": #Q.küçüldü ,q==q ise çıktı.
        print("Programdan çıkılıyor... Güvenle kalın!")
        break 
    if not password.strip(): # strip() boşlukları siler, yani sadece boşluk girse bile yakalarız
        print("⚠️ Lütfen bir şifre giriniz!")
        continue # Döngünün başına döner, aşağıdaki kodları çalıştırmaz

    buyuk_harf_var = False
    kucuk_harf_var = False
    rakam_var = False
    special_characters = string.punctuation # bu !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ karakterlerinin tamamını kapsar.
    ozel_karakter_var = False

    puan=0
    durum = "BİLİNMİYOR"
    for character in password:
        if character.isupper(): # "sen büyük harf misin?" diye sorar
            buyuk_harf_var = True
        elif character.islower(): # "sen küçük harf misin?" diye sorar
            kucuk_harf_var = True
        elif character.isdigit(): # "sen bir rakam misin?" diye sorar
            rakam_var = True
        elif character in special_characters:
            ozel_karakter_var = True

    eksikler = []

    if len(password) >= 8 and len(password) <= 50 : #uzunluk kontrolü (len fonksiyonu ile)
        puan+=20
    else:
        eksikler.append("- şifre doğru uzunlukta değil. (en az 8 karakter uzunluğunda olmalı)")
    if buyuk_harf_var:
        puan +=20
    else:
        eksikler.append("- Şifrede en az bir büyük harf olmalı.")
    if kucuk_harf_var:
        puan+=20
    else:
        eksikler.append("- Şifrede en az bir küçük harf olmalı.")
    if rakam_var:
        puan+=20
    else:
        eksikler.append("- Şifrede en az bir rakam olmalı.")
    if  ozel_karakter_var:
        puan+=20
    else:
        eksikler.append("- Şifrede en az bir özel karakter (!, @, # vb.) olmalı.")

    if not eksikler:
        durum = "MÜKEMMEL"
        print(f"Güvenlik Puanı: {puan}/100")
        print("✅ Şifreniz siber güvenlik standartlarına uygun.")
    else:
        if puan<=40 :     #0-1-2-3 madde iyi
            durum = "TEHLİKELİ"
        elif puan<=80 :  #4 madde iyi
            durum = "ORTA"
        print(f"Güvenlik Puanı: {puan}/100")
        print(f"❌ Şifrenizin durumu {durum} tespit edildi.")
        for madde in eksikler:
            print(madde)


    havuz = 0
    if kucuk_harf_var: havuz += 26
    if buyuk_harf_var: havuz += 26
    if rakam_var: havuz +=10
    if ozel_karakter_var: havuz += len(special_characters)
    # EĞER ŞİFREDE BOŞLUK VARSA HAVUZA +1 EKLE
    if " " in password:
        havuz += 1

    if havuz > 0:
        toplam_ihtimal = havuz ** len(password)
        # saniyede 1 milyar deneme yapan bir hacker cihazı varsayalım
        saniye = toplam_ihtimal / 1000000000
        dakika = saniye / 60
        saat = saniye / 3600
        gun = saat / 24
        # EN BÜYÜK BİRİMDEN BAŞLA
        if saat >= 8760: # 1 yıldan fazlaysa
            print("💡 Bu şifreyi kırmak yıllar sürebilir!")
            
        elif saat >= 24: # 1 yıldan az 1 günden büyük
            print(f"💡 Bu şifre yaklaşık {gun:.0f} günde kırılabilir.")

        elif saat >= 1: # 1 günden az 
            print(f"💡 Bu şifre yaklaşık {saat:.1f} saatte kırılabilir.")
            
        elif saniye >= 60: 
            print(f"💡 Bu şifre yaklaşık {dakika:.0f} dakikada kırılabilir.")
            
        elif saniye >= 1: 
            print(f"💡 Bu şifre yaklaşık {saniye:.0f} saniyede kırılabilir.")
            
        else:
            print("💡 Bu şifre anında (milisaniyeler içinde) kırılabilir!")      
