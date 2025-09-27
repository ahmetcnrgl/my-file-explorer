📂 Mini File Explorer (Python)

    İşlevsel bir komut satırı dosya gezginim
    
        🚀 Özellikler


            📑 Listeleme (list) → klasördeki dosya ve klasörleri boyut ve tarih bilgisiyle gösterir

            📂 Klasör değiştirme (cd) → çalışma dizinini değiştirir (.. desteği ile bir üst klasöre çıkış)

            ℹ️ Bilgi özeti (info) → dosya/klasör hakkında bilgi (boyut, oluşturulma tarihi, en büyük dosya vb.)

            🏗️ Klasör oluşturma (mkdir) → yeni klasör açar

            ✏️ Yeniden adlandırma (rename) → dosya veya klasör adı değiştirir

            🗑️ Silme (delete) → dosya veya boş klasörü siler, işlem öncesi onay ister

            ❓ Yardım (help) → kullanılabilir tüm komutları listeler

            🚪 Çıkış (quit) → programı sonlandırır
            

                💻 Menü

                    Mevcut klasör: C:/Users/Ahmet/Desktop
                    Komut giriniz: help

                    Komutlar:
                    list          → Klasördeki dosyaları listele
                    cd            → Klasör değiştir
                    info          → Dosya/klasör bilgisi
                    mkdir         → Yeni klasör oluştur
                    rename        → Yeniden adlandır
                    delete        → Dosya/klasör sil
                    quit          → Çıkış yap


                        📦 Proje Yapısı

                            .
                            ├── main.py              # Uygulama akışı
                            ├── listFunction.py      # list komutu
                            ├── cdFunction.py        # cd komutu
                            ├── infoFunction.py      # info komutu
                            ├── mkdirFunction.py     # mkdir komutu
                            ├── renameFunction.py    # rename komutu
                            ├── deleteFunction.py    # delete komutu
                            └── README.md            # Bu dosya

