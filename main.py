import os


# Yardım menüsü
def FileExpMenu():
    print(
        "*****Kullanabileceğiniz Komutlar*****  \n"
        "help : Yardım menüsünü gösterir.\n"
        "list : Bulunduğunuz dizindeki dosyaları ve klasörleri listeler. \n"
        "cd : Dizin değiştirmenizi sağlar. \n"
        "mkdir : Yeni bir klasör oluşturmanızı sağlar.\n"
        "info : Dosya ve klasör hakkında bilgi verir. \n"
        "rename : Dosya veya klasörün ismini değiştirmenizi sağlar. \n"
        "delete : Dosya veya klasörü silmenizi sağlar. \n"
        "quit : Programdan çıkmanızı sağlar.\n"
    )


# Menünün çağrılması, komutların işlenmesi ve şuanki dizinin gösterilmesi
def main():
    print("Merhaba! Şuanki dizininiz :", os.getcwd())
    print("\n")
    FileExpMenu()
    while True:
        # Kullanıcıdan alınan komutlardaki olası boşluklukları ve büyük harfleri engelledik.
        komut = input("Komut giriniz : ").strip().lower()
        if komut == "help":
            FileExpMenu()
            continue
        elif komut == "list":
            pass

        elif komut == "cd":
            pass

        elif komut == "mkdir":
            pass

        elif komut == "info":
            pass

        elif komut == "rename":
            pass

        elif komut == "delete":
            pass

        elif komut == "quit":
            print("Programdan çıkılıyor...")
            return False
        else:
            print(
                "Geçersiz komut girdiniz! help komutunu kullanarak yardım menüsüne ulaşabilirsiniz."
            )


if __name__ == "__main__":
    main()
