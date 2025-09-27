import os


def deleteDirectory():  # delete komutu için fonksiyon
    print("Mevcut dizin: ", os.getcwd(), "\n")
    silinecek = input(
        "Lütfen silmek istediğiniz klasörün veya dosyanın adını giriniz: "
    )
    silinecekYol = os.path.join(os.getcwd(), silinecek)
    # Yol var mı?
    if not os.path.exists(silinecekYol):
        print(f"Hata: '{silinecek}' bulunamadı.")
        return

        # Onay al
    onay = input(f"Emin misiniz '{silinecek}' silinsin mi? (y/n): ").lower()
    if onay != "y":
        print("İşlem iptal edildi.")
        return

    # Dosya mı klasör mü kontrolü
    if os.path.isfile(silinecekYol):
        os.remove(silinecekYol)
        print(f"Dosya silindi: {silinecek}")
    elif os.path.isdir(silinecekYol):
        try:
            os.rmdir(silinecekYol)
            print(f"Klasör silindi: {silinecek}")
        except OSError:
            print(f"Hata: '{silinecek}' klasörü boş değil, bu komutla silinemez.")
    else:
        print(f"Hata: '{silinecek}' ne dosya ne de klasör.")
