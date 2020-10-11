nama = "Gulnrz"

def ganti_nama():
    global nama
    nama = "Nazha"
    print("Variabel lokal: ",nama)

ganti_nama()
print("Variabel global: ",nama)