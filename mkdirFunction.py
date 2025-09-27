import os


def makeDirectory():  # mkdir fonsiyonu için komut
    print("Klasör oluşturmak için 1, iç içe klasörler oluşturmak için 2 yazınız \n")
    makeSecim = input()

    if makeSecim == "1":
        try:
            newDirectory = input("Oluşturmak istediğiniz klasörün adını giriniz: ")
            os.mkdir(newDirectory)
            print(f"Başarılı! '{newDirectory}' adlı klasör oluşturuldu.\n")
            print("Mevcut dizin:", os.getcwd(), "\n")
        except FileExistsError:
            print("Hata! Böyle bir klasör zaten mevcut.\n")
        except PermissionError:
            print("Hata! Bu dizine klasör oluşturma izniniz yok.\n")
        except OSError as e:
            print(f"Hata! Klasör oluşturulamadı : {e}\n")
        except Exception as e:
            print(f"Bilinmeyen bir hata oluştu: {e}\n")

    elif makeSecim == "2":
        try:
            newInnerDirectories = input(
                "Oluşturmak istediğiniz klasörlerin adlarını aralarında / işareti bırakarak giriniz: "
            )
            os.makedirs(newInnerDirectories, exist_ok=True)
            print(f"Başarılı! '{newInnerDirectories}' adlı klasörler oluşturuldu. \n")
            print("Mevcut dizin:", os.getcwd(), "\n")
        except PermissionError:
            print("Hata! Bu dizine klasör oluşturma izniniz yok. \n")
        except OSError as e:
            print(f"Hata! Klasörler oluşturulamadı : {e}\n")
        except Exception as e:
            print(f"Bilinmeyen bir hata oluştu: {e}\n")
    else:
        print("Geçersiz Seçim! Lütfen 1 veya 2 giriniz.\n")
