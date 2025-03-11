nama = input("Masukkan nama siswa : ")
NIM = input("Masukkan NIM : ")
Resolusi = input("Masukkan Resolusi Tahun ini : ")


with open("me.txt", "w") as f:
    f.write("nama siswa : " + nama + "\n")
    f.write("NIM : " + NIM + "\n")
    f.write("Resolusi Tahun ini : " + Resolusi + "\n")
    f.close()
print("Data berhasil disimpan!")
