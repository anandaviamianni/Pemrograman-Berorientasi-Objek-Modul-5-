# Ivan sedang mengerjakan soal FPB (Faktor Persekutuan Terbesar) dua bilangan. Kemudian Ivan berpikir bahwa soal FPB ini bisa diselesaikan dengan suatu program. Oleh karena itu, dia memanggil temannya yang merupakan seorang programmer. Bantulah Ivan membuat program FPB Matematika. FPB (Faktor Persekutuan Terbesar). Contoh FPB manual: ● Faktor dari 12 = 1, 2, 3, 4, 6 dan 12 ● Faktor dari 20 = 1, 2, 4, 5, 10 dan 20 ● FPB dari 12 dan 20 adalah faktor sekutu (sama) yang terbesar, yaitu 4. 

print("===== PROGRAM FPB DUA BILANGAN =====")
def FPB(a,b):
    #mencari bilangan yang paling kecil
    if(a < b):
        small = a
    else:
        small = b

    #mencari faktor persamaan
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            hasil_FPB = i
    
    return hasil_FPB

x = int(input("Masukan angka pertama \t: "))
y = int(input("Masukkan angka kedua \t: "))
print("FPB dari "+str(x)+" dan "+str(y)+" yaitu ", FPB(x,y))
