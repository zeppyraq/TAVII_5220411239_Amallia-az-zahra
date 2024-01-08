class Pertanian:
    def __init__(self, luas_lahan, jumlah_tanaman, jenis_pupuk):
        self.luas_lahan = luas_lahan
        self.jumlah_tanaman = jumlah_tanaman
        self.jenis_pupuk = jenis_pupuk

    def get_info(self):
        return f"Lahan:{self.luas_lahan}, Tanaman:{self.jumlah_tanaman}, Pupuk:{self.jenis_pupuk}"

# Buat subclass PertanianSayuran yang mewarisi Pertanian
class PertanianSayuran(Pertanian):
    def __init__(self, luas_lahan, jumlah_tanaman, jenis_pupuk, jenis_sayuran):
        super().__init__(luas_lahan, jumlah_tanaman, jenis_pupuk)
        self.jenis_sayuran = jenis_sayuran

    def tampilkan_info(self):
        print(f"Pertanian sayuran dengan luas lahan {self.luas_lahan}, menggunakan pupuk {self.jenis_pupuk}, dan menanam {self.jumlah_tanaman} tanaman {self.jenis_sayuran}.")

# Buat subclass PertanianBuah yang mewarisi Pertanian
class PertanianBuah(Pertanian):
    def __init__(self, luas_lahan, jumlah_tanaman, jenis_pupuk, jenis_buah):
        super().__init__(luas_lahan, jumlah_tanaman, jenis_pupuk)
        self.jenis_buah = jenis_buah

    def tampilkan_info(self):
        print(f"Pertanian buah dengan luas lahan {self.luas_lahan}, menggunakan pupuk {self.jenis_pupuk}, dan menanam {self.jumlah_tanaman} tanaman {self.jenis_buah}.")

# Contoh Implementasi Objek
kebun1 = Pertanian("100 ha", "1000", "Organik")
kebun2 = PertanianSayuran("250 ha", "3000", "Kompos", "Bayam")
kebun3 = PertanianBuah("500 ha", "2000", "Manis", "Stroberi")

info_kebun1 = kebun1.get_info()
info_kebun2 = kebun2.get_info()
info_kebun3 = kebun3.get_info()

print()
print('t\t\t1. KATEGORI PERTANIAN')
print(144*'=')
print(f"{info_kebun1}")

print()
print('t\t\t2. KATEGORI PERTANIAN SAYURAN')
print(144* '=')
print(f"{info_kebun2}, Pertanian sayuran dengan luas lahan {kebun2.luas_lahan}, menggunakan pupuk {kebun2.jenis_pupuk}, dan menanam {kebun2.jumlah_tanaman} tanaman {kebun2.jenis_sayuran}.")


print()
print('t\t\t3. KATEGORI PERTANIAN BUAH')
print(144* '=')
print(f"{info_kebun3}, Pertanian buah dengan luas lahan {kebun3.luas_lahan}, menggunakan pupuk {kebun3.jenis_pupuk}, dan menanam {kebun3.jumlah_tanaman} tanaman {kebun3.jenis_buah}.")
