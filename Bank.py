def Lihat(saldo):
    print(f"saldo anda tersisa: {saldo:.2f}")

def masukan():
    jumlah = float(input("masukan nominal deposit: "))

    if jumlah < 0:
        print("nominal tidak valid")
        return 0
    else:
        return jumlah

def tarik(saldo):
    jumlah = float(input("masukan nominal yang ingin diambil: "))

    if jumlah > saldo:
        print("saldo tidak mencukupi!")
        return 0
    elif jumlah < 0:
        print("nominal tidak valid!")
        return 0
    else:
        return jumlah
    
def main():
    saldo = 0
    jalan =  True

    while jalan:
        print("Bank Sederhana")
        print("1. Lihat Saldo")
        print("2. Masukan Saldo")
        print("3. Tarik Saldo")
        print("4. Keluar")

        pilih = int(input("Masukan Pilihan: "))

        if pilih == 1:
            Lihat(saldo)
        elif pilih == 2:
            saldo += masukan()
        elif pilih == 3:
            saldo -= tarik(saldo)
        elif pilih == 4:
            keluar = input("keluar? (y/n)")
            if keluar == "y":
                break
                

if __name__ == "__main__":
    main()