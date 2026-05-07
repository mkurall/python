#Ekrana menü seçeneklerini yazıran bir fonk yazın
#----MENU----
#1-Listele
#2-Yeni Ekle
#3-Sil
#4-Çıkış
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
DEFAULT = "\033[0m" 

veriler = {} #boş sözlük

def bekle():
    input(f"{GREEN}Devam etmek için <<Enter>> tuşunan basın.{DEFAULT}")

def menu_goster():
    print(f"{RED}----MENU-----{DEFAULT}")
    print(f"{BLUE}1-Listele")
    print(f"2-Yeni Ekle")
    print(f"3-Sil")
    print(f"4-Çıkış{DEFAULT}")

def secim_yap():
    while True:
        secim = int(input("Seçiminizi yapın:"))
        if secim not in [1,2,3,4]:
            print("Hatalı secim!")
            continue
        return secim

def listele():
    print("LİSTELENİYOR.........")
    for (tel, ad) in veriler.items():
        print(f"Tel: {tel} Ad Soyad: {ad}")
    bekle()
def yeni_ekle():
    print("YENİ KAYIT EKLENİYOR......")
    tel = input("Eklemek istediğiniz telefon numarası:")
    if tel in veriler:
        print("Zaten bu numara eklenmiş!")
    else:
        ad = input("Eklemek istediğiniz isim:")
        veriler[tel] = ad
    bekle()
def sil():
    print("SİLİNİYOR.......:.")
    tel = input("Silmek istediğiniz telefon numarası:")
    if tel in veriler:
        veriler.pop(tel)
    else:
        print("Bu numara bulunamadı!")
    bekle()
#ana Program Döngüsü
while True:
    menu_goster()
    secilen = secim_yap()
    print("Seçiminiz ", secilen)

    if secilen == 1:
        listele()
    elif secilen == 2:
        yeni_ekle ()
    elif secilen == 3:
        sil()
    else:
        print("Çıkış Yapılıyor...")
        break

