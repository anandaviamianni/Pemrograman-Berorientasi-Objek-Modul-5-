mangga = [20,21,30,40,50,30,40,20,25,46,38,40]
jambu = [25,24,40,44,60,37,21,29,50,55,60,42]

jumlah_buah = map(lambda x,y: x+y, mangga, jambu)
print("Hasil jumlah buah setiap bulannya yaitu\n", list(jumlah_buah))