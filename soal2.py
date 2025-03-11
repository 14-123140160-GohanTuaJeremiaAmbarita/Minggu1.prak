data_siswa = {}

jumlah_siswa = int(input("Masukkan jumlah siswa : "))

for i in range(jumlah_siswa):
    nama = input(f"Masukkan nama siswa ke-{ i + 1}  : ")
    nilai = int(input(f"Masukkan nilai siswa ke-{ i + 1} : "))
    data_siswa[nama] = nilai

print("\n dictionary data siswa : ", data_siswa)
