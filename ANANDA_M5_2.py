# List Sisi
sisi = [19, 21, 33, 17, 23, 51, 47, 41, 31, 11, 13]

# Fungsi di implementasikan dengan map()
hasil_sisi = map(lambda sisi: 6*sisi*sisi, sisi) 

# Menampilkan hasil data dan hasil permukaan luas
print("Berikut sisi-nya sesuai data soal:\n", sisi)
print("Hasil luas permukaan kubus masing-masing sisi yaitu:\n", list(hasil_sisi))