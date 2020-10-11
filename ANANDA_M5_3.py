# Membuat sebuah deklarasi menggunakan class
class Kubus():
    # Mendefinisikan variabel dengan sisi dan self
    def __init__(self, sisi):
        self.sisi = sisi

    # Memberikan fungsi rumus volume
    def volume(self):
        return self.sisi*self.sisi*self.sisi

    # Memberikan fungsi rumus luas
    def luas(self):
        return 6*self.sisi*self.sisi

    # Memberikan fungsi rumus keliling
    def keliling(self):
        return 12*self.sisi
    
    # # Menbrikan fungsi untuk menampilkan hasil kubus
    def tampil(self):
        volume = self.volume()
        luas = self.luas()
        keliling = self.keliling()
        print("Volume:\t\t", volume, "cm^3")
        print("Luas Permukaan:\t",luas, "cm^2")
        print("Keliling:\t", keliling, "cm", '\n')

#Inputan sisi kubus 1
kubus1 = Kubus(5)
#Inputkan sisi kubus 2
kubus2 = Kubus(10)

print('Kubus 1')
#Menampilkan hasil kubus 1
kubus1.tampil()
print('Kubus 2')
# Menampilkan hasil kubus 2
kubus2.tampil()