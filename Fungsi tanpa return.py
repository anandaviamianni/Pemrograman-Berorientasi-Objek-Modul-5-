listnama = ["Ivan", "Gufron", "Daniel", "Oji"]
def tambahNamaKeList(nama):
    listnama.append(nama)
    print(listnama)

tambahNamaKeList("Anton")

#or
# Perbedaan fungsi return dengan fungsi tanpa return adalah ketika fungsi tanpa return di print maka yang tampil adalah ‘None’ karena fungsi ini tidak mengembalikan nilai apapun. 
# listnama = ["Ivan", "Gufron", "Daniel", "Oji"]
# def tambahNamaKeList(nama):
#     listnama.append(nama)
#     print(listnama)

# print("Fungsi tanpa return diprint maka akan keluar --->", tambahNamaKeList("Anton"))