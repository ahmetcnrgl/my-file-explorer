import os


def infoDirectory():  # info komutu için fonksiyon
    print("Mevcut dizin:", os.getcwd(), "\n")
    bilgiSecim = input(
        "Bilgilerini öğrenmek istediğiniz dosya veya klasörün adını giriniz: "
    ).strip()
    yol = os.path.join(os.getcwd(), bilgiSecim)  # Dosya yolu
    if os.path.exists(yol):
        if os.path.isfile(yol):
            print(
                f'"{bilgiSecim}" bir dosyadır ve dosya boyutu {os.path.getsize(yol)} bytedır. \n'
            )
        elif os.path.isdir(yol):
            print(
                f'"{bilgiSecim}" bir klasördür ve içindeki öğe sayısı {len(os.listdir(yol))} dir. \n'
            )
        else:
            print("Bilinmeyen bir tür \n")
    else:
        print("Hata! Böyle bir dosya veya klasör bulunamadı.\n")
