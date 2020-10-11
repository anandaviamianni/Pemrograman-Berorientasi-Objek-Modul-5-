def luas_persegi_panjang(panjang = 10, lebar = 5):
    luas = panjang * lebar
    print("Panjang : ", panjang)
    print("Lebar : ",lebar)
    return luas

print("Tidak mengubah argument default")
print("Luas persegi panjang", luas_persegi_panjang())

print("\nMengubah argument default")
# dengan panjang = 8, lebar = 4
print("Luas persegi panjang", luas_persegi_panjang(8,4))