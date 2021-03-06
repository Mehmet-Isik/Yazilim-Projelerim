import time
import sqlite3


def tesekkür():
    print("*****M.I Otomasyonlarını Tercih Ettiginiz Icin Tesekkur Ederiz.***** :))\n"
          "Kolay gelsin, iyi tarimlar ve bol bereketli topraklar dileriz.\n\n\n\n")
    return



def cikis():
    print("çikiliyor...\n")
    time.sleep(1)
    print("Otomasyon'dan cikildi.!!!\n")
    return



def Sonbahar():
    print("1-Eylul\n")
    print("2-Ekim\n")
    print("3-Kasim\n")

    while True:
        aylar = input("Aylardan birini seçiniz:\n\n")

        try:
            aylar = int(aylar)
            if aylar == 1:
                print("Misir --> Sicaklik: 16-32°C\nToprak pH: 6.5-7.0\n\n"
                      "Ispanak --> Sicaklik: 15-20°C\nToprak pH: 6.5-7.5\n\n"
                      "Biberiye --> Sicaklik: 20-25°C\nToprak pH: 6.0-6.5\n\n")

            elif aylar == 2:
                print("Bakla --> Sicaklik: 10-20°C \nToprak pH: 6.7-7.2\n\n"
                      "Dereotu --> Sicaklik: 20-30°C\nToprak pH: 0.5-7.5\n\n"
                      "Roka --> Sicaklik: 20-25°C\nToprak pH: 7.0\n\n")

            elif aylar == 3:
                print("Bezelye --> Sicaklik: 12–18°C\nToprak pH: 5.5-6.7\n\n"
                      "Sarimsak --> Sicaklik: 15-20°C\nToprak pH: 6.5-7.0\n\n"
                      "Sogan --> Sicaklik: 12-13°C\nToprak pH: 6.0- 6.5"
                      "\n\n")

            else:
                print("Hatali islem!!!\n\n")
                continue
            tesekkür()
            break
        except:
            print("Sadece sayi giriniz!!!\n")
            continue
            return



def Kis():
    print("1-Aralik\n")
    print("2-Ocak\n")
    print("3-Subat\n")

    while True:
        aylar = input("Aylardan birini seçiniz:\n\n")

        try:
            aylar = int(aylar)
            if aylar == 1:
                print("Bugday --> Sicaklik: 10-15°C\nToprak pH: 6.5-7.0\n\n"
                      "Yulaf --> Sicaklik: 10-15°C\nToprak pH: 6.5-7.0\n\n"
                      "Cavdar --> Sicaklik: 10-15°C\nToprak pH: 6.5-7.0\n\n")

            elif aylar == 2:
                print("Patlican --> Sicaklik: 15-35°C\nToprak pH: 6.0-7.0\n\n"
                      "Maydonoz --> Sicaklik: 15-25°C\nToprak pH: 5.0-8.0\n\n"
                      "Karnabahar --> Sicaklik: 15°C-20°C\nToprak pH: 5.5-6.5\n\n")

            elif aylar == 3:
                print("Ceri Domates --> Sicaklik: 18-27°C\nToprak pH: 5.5-7.0\n\n"
                      "Carliston Biber --> Sicaklik: 20-25°C\nToprak pH: 6.0-6.5\n\n"
                      "Dereotu --> Sicaklik: 20-30°C\nToprak pH: 0.5-7.5\n\n")

            else:
                print("Hatali islem!!!\n\n")
                continue
            tesekkür()
            break
        except:
            print("Sadece sayi giriniz!!!\n")
            continue
            return



def Ilkbahar():
    print("1-Mart\n")
    print("2-Nisan\n")
    print("3-Mayis\n")

    while True:
        aylar = input("Aylardan birini seçiniz:\n\n")

        try:
            aylar = int(aylar)
            if aylar == 1:
                print("Dereotu --> Sicaklik: 20-30°C\nToprak pH: 0.5-7.5\n\n"
                      "Havuc --> Sicaklik: 15-30°C\nToprak pH: 6.0-6.5 \n\n"
                      "Beyaz Kabak --> Sicaklik: 10-25°C\nToprak pH: 6.0-7.0\n\n")

            elif aylar == 2:
                print("Salatalik --> Sicaklik: 20-30°C\nToprak pH:  5.5-5.8\n\n"
                      "Domates --> Sicaklik: 18-27°C\nToprak pH: 5.5-7.0\n\n"
                      "Roka --> Sicaklik:20-30°C\nToprak pH: 7.0\n\n")

            elif aylar == 3:
                print("Fasulye --> Sicaklik: 20-25°C\nToprak pH: 6.0-7.5\n\n"
                      "Bezelye --> Sicaklik: 18–21°C\nToprak pH: 5.5-6.7\n\n"
                      "Brokoli --> Sicaklik: 18-24°C\nToprak pH: 6.5-8.0\n\n")

            else:
                print("Hatali islem!!!\n\n")
                continue
            tesekkür()
            break
        except:
            print("Sadece sayi giriniz!!!\n")
            continue
            return



def Yaz():
    print("1-Haziran\n")
    print("2-Temmuz\n")
    print("3-Agustos\n")

    while True:
        aylar = input("Aylardan birini seçiniz:\n\n")

        try:
            aylar = int(aylar)
            if aylar == 1:
                print("Borulce --> Sicaklik: 20-30°C\nToprak pH: 5.5-6.5\n\n"
                      "Maydonoz --> Sicaklik: 15-25°C\nToprak pH: 5.0-8.0\n\n"
                      "Karnabahar --> Sicaklik: 15°C-20°C\nToprak pH: 5.5-6.5\n\n")

            elif aylar == 2:
                print("Misir --> Sicaklik: 16-32°C\nToprak pH: 6.5-7.0\n\n"
                      "Fasulye --> Sicaklik: 20-25°C\nToprak pH: 6.0-7.5\n\n"
                      "Havuc --> Sicaklik: 15-30°C\nToprak pH: 6.0-6.5 \n\n")

            elif aylar == 3:
                print("Roka --> Sicaklik:20-30°C\nToprak pH: 7.0\n\n"
                      "Borulce --> Sicaklik: 20-30°C\nToprak pH: 5.5-6.5\n\n"
                      "Ispanak --> Sicaklik:15-25°C\nToprak pH: 6.5-7.5\n\n")

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
    secenekler = input("\n(1)Otomasyon'a Giris\n(2)Uye Kaydi\n-->NOT(Eger Uye Kaydininiz Yoksa Once Uye Olunuz.!!!)\n\n")

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
                print("\n\nBu bilgilere ait bir kullanici bulunamadi.!!! Tekrar deneyiniz.\n")
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
        print("Hatali tuslama yaptiniz.!!!\n")
        continue
    print("\nArtik otomasyon'a giris yapabilirsiniz.\n")

ad.commit()
ad.close()


liste=["""(1) Sonbahar
(2) Kis
(3) Ilkbahar
(4) Yaz\n\n"""]
for i in liste:
    print(i)


while True:
    print("^^ Bilgiler Yukarida Yer Almaktadir. ^^\n ")
    print("***M.I OTOMASYON***\n")
    print("(M.I Tarla Otomasyon'una Hosgeldiniz.)\n")
    print("-->NOT:Bu otomasyon'da hangi aylarda, hangi ekinleri, hangi sartlarda,\n"
          "ekebileceginiz hakkında bilgi sahibi olabilirsiniz.\n")
    print("-->NOT: Otomasyonda verilen sicaklik ve pH degerleri optimum degeler olup,\n"
          "sadece o degelerde yetisecegi anlamina gelmemektedir.\n"
          "Ortalama o degerlerde istediginiz urunu yetistirebilirsiniz.\n")
    print("^^ Bilgiler Yukarida Yer Almaktadir. ^^\n\n ")

    kategori = input("Mevsim seciniz (Cıkmak icin 0'a basiniz.):\n")

    if kategori == "0":
        cikis()
        break

    elif kategori == "1":
            Sonbahar()

    elif kategori == "2":
        Kis()

    elif kategori == "3":
        Ilkbahar()

    elif kategori == "4":
        Yaz()
