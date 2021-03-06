import time
import sqlite3

def tesekkür():
    print("*****Magazamizi Tercih Ettiginiz Icin Tesekkur Ederiz.***** :))\n\n\n\n")
    return



def cikis():
    print("çikiliyor...\n")
    time.sleep(1)
    print("sistemden cikildi.!!!\n")
    return



def bilgisayar():
    print("1-Laptop\n")
    print("2-Masaustu\n")

    tip = input("Bilgisayar tipini seciniz:\n")

    if tip == "1":
        print("1-M.I-LS --> (2000 tl)\n\n (2gb ram)\n (2gb ekran karti)\n (500gb hdd)\n (i3-6.nesil)\n\n")
        print("2-M.I-LM --> (4000 tl)\n\n (4gb ram)\n (4gb ekran karti)\n (1tb hdd + 256gb ssd)\n (i5-7.nesil)\n\n")
        print("3-M.I-LL --> (8000 tl)\n\n (8gb ram)\n (6gb ekran karti)\n (256gb hdd + 1tb ssd)\n (i7-9.nesil)\n\n")

        while True:
            model = input("Bilgisayar modelini seciniz:\n\n")

            try:
                model = int(model)
                if model == 1:
                    print("--->>> ODENECEK TUTAR: 2000 tl.\n\n")

                elif model == 2:
                    print("--->>> ODENECEK TUTAR: 4000 tl.\n\n")

                elif model == 3:
                    print("--->>> ODENECEK TUTAR: 8000 tl.\n\n")

                else:
                    print("Hatali islem!!!\n\n")
                    continue
                tesekkür()
                break
            except:
                print("Sadece sayi giriniz!!!\n")
                continue

    if tip == "2":
        print("1-M.I-MSS --> (1500 tl)\n\n (2gb ram)\n (2gb ekran karti)\n (500gb hdd)\n (i3-6.nesil)\n\n")
        print("2-M.I-MSM --> (3500 tl)\n\n (4gb ram)\n (4gb ekran karti)\n (1tb hdd + 256gb ssd)\n (i5-7.nesil)\n\n")
        print("3-M.I-MSL --> (6500 tl)\n\n (8gb ram)\n (6gb ekran karti)\n (256gb hdd + 1tb ssd)\n (i7-9.nesil)\n\n")

        while True:
            model = input("Bilgisayar modelini seciniz:\n\n")
            try:
                model = int(model)
                if model == 1:
                    print("--->>> ODENECEK TUTAR: 1500 tl.\n\n")

                elif model == 2:
                    print("--->>> ODENECEK TUTAR: 3500 tl.\n\n")

                elif model == 3:
                    print("--->>> ODENECEK TUTAR: 6500 tl.\n\n")

                else:
                    print("Hatal islem!!!\n\n")
                    continue
                tesekkür()
                break
            except:
                print("Sadece sayi giriniz!!!\n")
                continue
                return



def telefon():
    print("1-M.I-xt20 --> (1000 tl)\n\n (2gb ram)\n (32gb hafiza)\n (xt-200 islemci)\n\n")
    print("2-M.I-xt40 --> (2500 tl)\n\n (4gb ram)\n (64gb hafiza)\n (xt-400 islemci)\n\n")
    print("3-M.I-xt80 --> (4000 tl)\n\n (8gb ram)\n (128gb hafiza)\n (xt-800 islemci)\n\n")

    while True:
        model = input("Telefon modelini seciniz:\n\n")

        try:
            model = int(model)
            if model == 1:
                print("--->>> ODENECEK TUTAR: 1000 tl.\n\n")

            elif model == 2:
                print("--->>> ODENECEK TUTAR: 2500 tl.\n\n")

            elif model == 3:
                print("--->>> ODENECEK TUTAR: 4000 tl.\n\n")

            else:
                print("Hatali islem!!!\n\n")
                continue
            tesekkür()
            break
        except:
            print("Sadece sayi giriniz!!!\n")
            continue
            return



def tablet():
    print("1-M.I-mt93x --> (1250 tl)\n\n (2gb ram)\n (64gb hafiza)\n (mtx-930 islemci)\n\n")
    print("2-M.I-wt46x --> (2750 tl)\n\n (4gb ram)\n (128gb hafiza)\n (wtx-460 islemci)\n\n")

    while True:
        model = input("Tablet modelini seciniz:\n\n")

        try:
            model = int(model)
            if model == 1:
                print("--->>> ODENECEK TUTAR: 1250 tl.\n\n")

            elif model == 2:
                print("--->>> ODENECEK TUTAR: 2750 tl.\n\n")

            else:
                print("Hatali islem!!!\n\n")
                continue
            tesekkür()
            break
        except:
            print("Sadece sayi giriniz!!!\n")
            continue
            return



def kamera():
    print("1-Aksiyon Kamerasi\n")
    print("2-Guvenlik Kamerasi\n")
    print("3-Arac Kamerasi\n")

    tip = input("Kamera tipini seciniz:\n")

    if tip == "1":
        print("1-M.I-ak-1 --> (500 tl)\n\n (12MP)\n (hd cozunurluk)\n (2.0 inch)\n\n")
        print("2-M.I-ak-2 --> (1000 tl)\n\n (24MP)\n (full hd cozunurluk)\n (2.0 inch)\n\n")
        print("3-M.I-ak-3 --> (1500 tl)\n\n (48MP)\n (ultra hd cozunurluk)\n (2.0 inch)\n\n")

        while True:
            model = input("Kamera modelini seciniz:\n\n")

            try:
                model = int(model)
                if model == 1:
                    print("--->>> ODENECEK TUTAR: 500 tl.\n\n")

                elif model == 2:
                    print("--->>> ODENECEK TUTAR: 1000 tl.\n\n")

                elif model == 3:
                    print("--->>> ODENECEK TUTAR: 1500 tl.\n\n")

                else:
                    print("Hatali islem!!!\n\n")
                    continue
                tesekkür()
                break
            except:
                print("Sadece sayi giriniz!!!\n")
                continue

    if tip == "2":
        print("1-M.I-gkd --> (1500 tl)\n\n (24MP)\n (full hd cozunurluk)\n\n")
        print("2-M.I-gki --> (2500 tl)\n\n (48MP)\n (ultra hd cozunurluk)\n (gece goruslu)\n\n")

        while True:
            model = input("Kamera modelini seciniz:\n\n")

            try:
                model = int(model)
                if model == 1:
                    print("--->>> ODENECEK TUTAR: 1500 tl.\n\n")

                elif model == 2:
                    print("--->>> ODENECEK TUTAR: 2500 tl.\n\n")

                else:
                    print("Hatali islem!!!\n\n")
                    continue
                tesekkür()
                break
            except:
                print("Sadece sayi giriniz!!!\n")
                continue

    if tip == "3":
        print("1-M.I-aik --> (1250 tl)\n\n (24MP)\n (full hd cozunurluk)\n (gps)\n\n")
        print("2-M.I-adk --> (1750 tl)\n\n (48MP)\n (ultra hd cozunurluk)\n (gece goruslu)\n (gps)\n\n")

        while True:
            model = input("Kamera modelini seciniz:\n\n")

            try:
                model = int(model)
                if model == 1:
                    print("--->>> ODENECEK TUTAR: 1250 tl.\n\n")

                elif model == 2:
                    print("--->>> ODENECEK TUTAR: 1750 tl.\n\n")

                else:
                    print("Hatali islem!!!\n\n")
                    continue
                tesekkür()
                break
            except:
                print("Sadece sayi giriniz!!!\n")
                continue
                return



def kulaklik():
    print("1-Kablolu Kulaklik\n")
    print("2-Kablosuz Kulaklik\n")

    tip = input("Kulaklik tipini seciniz:\n")

    if tip == "1":
        print("1-M.I-klk24 --> (75 tl)\n\n (Kulak ici kulaklik)\n (Frekans:20 Hz)\n (Duyarlilik: 93.2 dB)\n (Direnç: 32 Ohm)\n\n")
        print("2-M.I-klk42 --> (150 tl)\n\n (Kulak ustu kulaklik)\n (Frekans:20 Hz)\n (Duyarlilik: 93.2 dB)\n (Direnç: 32 Ohm)\n\n")

        while True:
            model = input("kulaklik modelini seciniz:\n\n")

            try:
                model = int(model)
                if model == 1:
                    print("--->>> ODENECEK TUTAR: 75 tl.\n\n")

                elif model == 2:
                    print("--->>> ODENECEK TUTAR: 150 tl.\n\n")

                else:
                    print("Hatali islem!!!\n\n")
                    continue
                tesekkür()
                break
            except:
                print("Sadece sayi giriniz!!!\n")
                continue

    if tip == "2":
        print("1-M.I-ksk12 --> (100 tl)\n\n (Kulak içi kulaklik)\n (Bluetooth: V5.0)\n (Batarya: 310 mAh)\n (Şarj Olma Suresi: 1.5 Saat)\n (Çalışma Menzili: 10m)\n\n")
        print("2-M.I-ksk21 --> (200 tl)\n\n (Kulak ustu kulaklik)\n (Bluetooth: V5.0)\n (Batarya: 310 mAh)\n (Şarj Olma Suresi: 1.5 Saat)\n (Çalışma Menzili: 10m)\n\n")

        while True:
            model = input("kulaklik modelini seciniz:\n\n")

            try:
                model = int(model)
                if model == 1:
                    print("--->>> ODENECEK TUTAR: 100 tl.\n\n")

                elif model == 2:
                    print("--->>> ODENECEK TUTAR: 200 tl.\n\n")

                else:
                    continue
                tesekkür()
                break
            except:
                print("Sadece sayi giriniz!!!\n")
                continue
                return



def drone():
    print("1-M.I-dx2w4 --> (750 tl)\n\n (boyutu: 40x40x7cm)\n (agirlik: 98gr)\n (cekim mesafesi 100m)\n (ucus suresi: 10-15dk)\n (sarj suresi: 50dk)\n\n")
    print("2-M.I-dx4w8 --> (1500 tl)\n\n (boyutu: 60x60x10cm)\n (agirlik: 131gr)\n (cekim mesafesi 250m)\n (ucus suresi: 20-25dk)\n (sarj suresi: 90dk)\n (kamera: 8Mp)\n\n")

    while True:
        model = input("Drone modelini seciniz:\n\n")

        try:
            model = int(model)
            if model == 1:
                print("--->>> ODENECEK TUTAR: 750 tl.\n\n")

            elif model == 2:
                print("--->>> ODENECEK TUTAR: 1500 tl.\n\n")

            else:
                print("Hatali islem!!!\n\n")
                continue
            tesekkür()
            break
        except:
            print("Sadece sayi giriniz!!!\n")
            continue
            return



veri = []
ad = sqlite3.connect("Mehmet.Mehmet")
y = ad.cursor()
y.execute("Create Table if not exists kullanici_arsivi (Kullanici_adi, Parola)")

while True:
    deneme = 0
    secenekler = input("\n(1)Alisveris Sitesine Giris\n(2)Uye Kaydi\n-->NOT(Eger Uye Kaydininiz Yoksa Once Uye Olunuz.!!!)\n\n")

    if secenekler == "1":
        while True:
            kulladi = input("\nKullanici adinizi giriniz  :")
            password = input("\n\nParolanizi giriniz  :")
            y.execute("SELECT * FROM kullanici_arsivi WHERE Kullanici_adi = ? and Parola = ?  ", (kulladi, password))
            data = y.fetchone()
            if data:
                print("\nBasariyla Giris Yapildi.\n")
                break
            else:
                print("\n\nBu bilgilere ait bir kullanici bulunamadi. Tekrar deneyiniz.\n")
                deneme = 1
                break
        if deneme == 1:
            continue
        break

    elif secenekler == "2":
        while True:
            bilgi_kulladi = input("\nBir kullanici adi giriniz : \n")
            if len(bilgi_kulladi) < 6 or len(bilgi_kulladi) > 18:
                print("\nLutfen 6 dan buyuk ve 18 den kucuk karakter sayisi ile kullanici adi giriniz.\n\n")
                continue
            else:
                bilgi_password = input("\nBir parola giriniz : \n")
                if len(bilgi_password) < 6 or len(bilgi_password) > 18:
                    print("\n\nLutfen 6 dan buyuk ve 18 den kucuk karakter sayisi ile parola giriniz.\n\n")
                    continue
                elif bilgi_password.isalpha == True:
                    print("\nLutfen sadece harf girmeyiniz.\n")
                    continue
                elif bilgi_password.isdigit() == True:
                    print("\nLutfen sadece sayi girmeyiniz.\n")
                    continue
                elif bilgi_password.isspace() == True:
                    print("\nLutfen bosluk kullanmayiniz.\n")
                    continue
                else:
                    veri += [bilgi_kulladi, bilgi_password]
                    y.execute("insert into kullanici_arsivi values (?, ?)", veri)
                    print("\nBasariyla kayit olundu.\n")
                    break

    else:
        print("Hatali tuslama yaptiniz.\n")
        continue
    print("\nArtik alisveris sitesine giris yapabilirsiniz.\n")

ad.commit()
ad.close()


liste=["""(1) Bilgisayar
(2) Telefon
(3) Tablet
(4) Kamera
(5) Kulaklik
(6) Drone\n\n"""]
for i in liste:
    print(i)

while True:
    print("***M.I TEKNOWORLD***\n")
    print("(M.I TeknoWorld'e Hosgeldiniz.)\n")
    kategori = input("Kategori seciniz (Cıkmak icin 0'a basiniz.):\n")

    if kategori == "0":
        cikis()
        break

    elif kategori == "1":
            bilgisayar()

    elif kategori == "2":
        telefon()

    elif kategori == "3":
        tablet()

    elif kategori == "4":
        kamera()

    elif kategori == "5":
        kulaklik()

    elif kategori == "6":
        drone()



