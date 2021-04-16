import random
def program():
    judul = "PROGRAM PEMILIHAN ASLAB PENDAMPING"
    print(judul.center(70,'-'))
    list = ["Aditya Mahendra","Andhika Pratama Putra","Muhammad Abyan Naufal","Muhammad Wildan Rusydani","Tiffany Bella Nagari"]
    print("Berikut daftar aslab pendamping untuk Praktikum Programa Komputer:")
    print(list)
    aslab = random.choice(list)
    x = input("Masukkan Nama Lengkap:")
    nama = x.upper()
    y = input("Masukkan NIM:")
    nim = y.capitalize()
    print("")
    print("SELAMAT!!! Aslab pendamping untuk",nama,"dengan NIM",nim,"adalah",aslab.upper())
program()