def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        return "Napaka: Deljenje z nič ni dovoljeno!"
    return a / b

print("Pozdrav! Mini kalkulator")

while True:
    print("\n--- MENI ---")
    print("1 = seštevanje")
    print("2 = odštevanje")
    print("3 = množenje")
    print("4 = deljenje")
    print("0 = IZHOD")

    izbira = input("Kaj želiš narediti? (0-4): ")

    if izbira == "0":
        print("Hvala, ker si uporabljal kalkulator. Nasvidenje!")
        break

    if izbira in ["1", "2", "3", "4"]:
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))

        if izbira == "1":
            print(f"--> IZRAČUN: {x} + {y} = {sestej(x, y)}")
        elif izbira == "2":
            print(f"--> IZRAČUN: {x} - {y} = {odstej(x, y)}")
        elif izbira == "3":
            print(f"--> IZRAČUN: {x} * {y} = {pomnozi(x, y)}")
        elif izbira == "4":
            rezultat = deli(x, y)
            if isinstance(rezultat, str):
                print(f"--> {rezultat}")
            else:
                print(f"--> IZRAČUN: {x} / {y} = {rezultat}")
    else:
        print("Neveljavna izbira, poskusi ponovno.")
