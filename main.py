from cdFunction import changeDirectory
from listFunction import listDirectory
from mkdirFunction import makeDirectory
from infoFunction import infoDirectory
from renameFunction import renameDirectory
from deleteFunction import deleteDirectory
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
            listDirectory()

        elif komut == "cd":
            changeDirectory()

        elif komut == "mkdir":
            makeDirectory()

        elif komut == "info":
            infoDirectory()

        elif komut == "rename":
            renameDirectory()

        elif komut == "delete":
            deleteDirectory()

        elif komut == "quit":
            print("Programdan çıkılıyor...")
            return False
        else:
            print(
                "Geçersiz komut girdiniz! help komutunu kullanarak yardım menüsüne ulaşabilirsiniz."
            )


if __name__ == "__main__":
    main()
