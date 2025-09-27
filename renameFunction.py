import os


def renameDirectory():  # rename komutu için fonksiyon
    print("Mevcut dizin: ", os.getcwd(), "\n")
    oldName = input("Adını değiştirmek istediğiniz dosyanın adını giriniz: ")
    newName = input("Yeni adı giriniz: ")
    oldPath = os.path.join(os.getcwd(), oldName)
    newPath = os.path.join(os.getcwd(), newName)
    try:
        os.rename(oldPath, newPath)
        print(
            f"Başarılı '{oldName}' adlı dosyanızın ismi '{newName}' olarak değiştirildi\n"
        )
    except FileExistsError:
        print("Hata! Böyle bir dosya zaten mevcut.\n")
    except PermissionError:
        print("Bu dosya üzerinde yetkiniz yok\n")
    except FileNotFoundError:
        print("Hata! Böyle bir dosya bulunamadı. \n")
    except OSError as e:
        print(f"Hata! Dosya ismi değiştirelemedi : {e}\n")
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu: {e}\n")
