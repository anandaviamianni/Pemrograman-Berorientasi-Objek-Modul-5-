# Memasukkan awalan angka pada variabel count
count = 0
# Inisialisasi def
def angka_prima(batas):
    for i in range(1,batas + 1): 
        if i > 1: 
            for j in range(2,i): 
                if (i % j) == 0: 
                    break 
            else:
                global count
                count += 1 

#Masukkan inputan pada Angka Batas
angka_batas = int(input('Masukan angka batas : '))
#Memasukkan isi dari variabel angka_prima pada angka_batas
angka_prima(angka_batas)
#Menampilkan hasil dari batas
print("Bilangan prima mulai dari 1 sampai",angka_batas,"ada sebanyak :",count)