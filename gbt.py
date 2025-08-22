import random

def gbt():
    # computer
    choices = ["gunting","batu","kertas"]
    # com = random.choice(choices)
    acak = random.randint(0,2)
    com = choices[acak]

    # user
    user = str(input("Masukan pilihan (gunting, batu kertas): ")).lower()

    # validasi
    while user not in choices:
        print("Pilihan tidak valid!")
        user = str(input("Masukan pilihan (gunting, batu kertas): ")).lower()

    if user == com:
        print(f"seri! kamu: {user} vs lawanmu: {com}")
    elif (user == "gunting" and com == "kertas") or \
         (user == "batu" and com == "gunting") or \
         (user == "kertas" and com == "batu"):
        print(f"kamu menang! kamu: {user} vs lawanmu: {com}")
    else:
        print(f"kamu kalah! kamu: {user} vs lawanmu: {com}")

if __name__ == "__main__":
    while True:
        print("game gunting batu kertas")
        gbt()

        mainkan_lagi = input("main lagi? (y/n): ").lower()
        if mainkan_lagi == "n":
            print("game selesai")
            break