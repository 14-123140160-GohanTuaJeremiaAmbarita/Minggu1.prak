tinggi = int(input("Masukkan tinggi: "))

for i in range(0, tinggi):
    for j in range(i, tinggi - 1):
        print(" ", end=" ")

    for j in range(tinggi - i, tinggi + 1):
        print("*", end=" ")

    for j in range(tinggi - i, tinggi):
        print("*", end=" ")

    print(" ")
