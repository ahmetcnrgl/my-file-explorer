import os
import datetime


def listDirectory():  # list komutu için fonksiyon
    dosyaSayac = 0
    klasorSayac = 0
    dosyalar = os.listdir()

    print(
        f'{"Ad":40} | {"Tür":7} | {"Boyut (B)":11} | Son Değişiklik'
    )  # Tablo sütun başlıkları
    print("-" * 85)
    # Dosyaların ve klasörlerin listelenmesi
    for dosya in dosyalar:
        yol = os.path.join(os.getcwd(), dosya)  # dosya yolu

        if os.path.isfile(yol):
            boyut = os.path.getsize(yol)  # dosya boyutu
            tarih = datetime.datetime.fromtimestamp(os.path.getmtime(yol)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )  # dosyanın son değiştirilme tarihi
            print(f'{dosya:40} | {"DOSYA":7} | {boyut:11,} | {tarih}')
            dosyaSayac += 1

        elif os.path.isdir(yol):
            print(f"{dosya:40} | {"KLASÖR":7} | {"":11} | {"":19}")
            klasorSayac += 1

    print("-" * 85)
    print(f"Toplam {dosyaSayac} dosya ve {klasorSayac} klasör bulunmaktadır.\n")
