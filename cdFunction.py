import os


def changeDirectory():  # cd komutu için fonksiyon
    print("Mevcut dizin:", os.getcwd(), "\n")
    print(
        "Herhangi bir dizine gitmek için 1, bir üst dizine gitmek için 2, ana dizine gitmek için 3 yazınız."
    )
    secim = input("Seçiminiz: ").strip()
    if secim == "1":  # Kullanıcının seçimine göre dizin değiştirme işlemleri
        yeniDizin = input("Gitmek istediğiniz dizin yolunu giriniz : ").strip()
        try:
            os.chdir(yeniDizin)
            print("Başarılı! Şuanki dizin:", os.getcwd(), "\n")
        except FileNotFoundError:
            print("Hata! Böyle bir dizin bulunamadı.\n")
        except NotADirectoryError:
            print("Hata! Belirtilen yol bir dizin değil.\n")
        except PermissionError:
            print("Hata! Bu dizine erişim izniniz yok.\n")

    elif secim == "2":
        try:
            os.chdir("..")
            print("Başarılı! Şuanki dizin:", os.getcwd(), "\n")
        except PermissionError:
            print("Hata! Bir üst dizine erişim izniniz yok.\n")

    elif secim == "3":
        try:
            os.chdir(os.path.abspath(os.sep))
            print("Başarılı! Şuanki dizin: ", os.getcwd(), "\n")
        except PermissionError:
            print("Hata! Ana dizine erişim izniniz yok.\n")

    else:
        print("Geçersiz seçim yaptınız!\n")
