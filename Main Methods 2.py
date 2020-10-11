class Komputer():
    def menyala(self):
        print("-"*20, "D2GF Computer", "-" * 20)
        print("Komputer dinyalakan.\nSelamat datang, semoga harimu menyenangkan :)")

    def shutdown(self):
        print("-" * 20, "D2GF Computer", "-" * 20)
        print("Komputer dimatikan, selamat tinggal")

if __name__ == "__main__":
    com1 = Komputer()
    com1.menyala()
    print()
    com1.shutdown()