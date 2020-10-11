class Kolam():
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    def volume(self):
        return self.panjang * self.lebar * self.tinggi
    def tampil (self):
        volume = self.volume()
        harga = harga_total(volume)
        print("Panjang : ", self.panjang)
        print("Lebar : ", self.lebar)
        print("Tinggi : ", self.tinggi)
        print("Volume : ", volume)
        print("Harga : ", harga)
        print("="*10)

harga_per_m3 = int(input("Harga per m^3 : "))
harga_total = lambda volume: volume * harga_per_m3

k1 = Kolam ( 20, 10, 2)
k2 = Kolam (10, 6, 1)

k1.tampil()
k2.tampil()