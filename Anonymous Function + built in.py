tuple_num = (1,2,3,4,5,6,7)
result_map = map(lambda item: item ** 2, tuple_num)
result_filter = filter(lambda item : item % 2 != 0, tuple_num)

print("Tuple default :\n ",tuple_num)
print("Tuple baru dengan isi dikuadratkan 2:\n ", tuple(result_map))
print("Tuple baru dengan nilai ganjil saja yang ditampilkan:\n ",tuple(result_filter))