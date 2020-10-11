class Mamalia:
    def __init__(self, jenis, nama, makanan, habitat):
        self.jenis = jenis
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
    
    def detail(self):
        print("Nama Hewan\t\t: ",self.nama)
        print("Jenis Hewan\t\t: ",self.jenis)
        print("Habitat Hewan\t: ",self.habitat)
        print("Makanan Hewan\t: ",self.makanan)

class HewanLaut(Mamalia):
    def cara_bergerak(self):
        print("Cara bergerak\t: Berenang")

paus = HewanLaut("Paus","Blue","Plankton","Laut")
paus.detail()
paus.cara_bergerak()

print()
# lumbalumba = HewanLaut("Lumba-Lumba","Pinoo","Herring","Udang","Laut")
# lumbalumba.detail()
# lumbalumba.cara_bergerak()