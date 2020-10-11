# Cara 1 dimasukkan ke variabel dulu
result = lambda x,y : x**2 + y**2
print("Hasil lambda dimasukkan ke variabel\n", result(5,10))

# Cara 2 langsung print
print("\nHasil langsung print")
print((lambda x,y : x ** 2 + y ** 2)(4,6))