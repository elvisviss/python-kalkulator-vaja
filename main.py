def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z nič!"
    return a / b

zgodovina = [] 

print("Pozdrav! Mini kalkulator s spominom")

while True:
    print("\n--- MENI ---")
    print("1 = seštevanje | 2 = odštevanje | 3 = množenje | 4 = deljenje")
    print("5 = PRIKAŽI ZGODOVINO")
    print("0 = IZHOD")

    izbira = input("Izbira: ")

    if izbira == "0":
        print("Nasvidenje!")
        break
    
    if izbira == "5":
        print("\n--- ZADNJI 3 IZRAČUNI ---")
        if not zgodovina:
            print("Zgodovina je prazna.")
        for vpis in zgodovina:
            print(vpis)
        continue

    if izbira in ["1", "2", "3", "4"]:
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        operacija = ""
        rezultat = 0

        if izbira == "1":
            rezultat = sestej(x, y)
            operacija = f"{x} + {y} = {rezultat}"
        elif izbira == "2":
            rezultat = odstej(x, y)
            operacija = f"{x} - {y} = {rezultat}"
        elif izbira == "3":
            rezultat = pomnozi(x, y)
            operacija = f"{x} * {y} = {rezultat}"
        elif izbira == "4":
            rezultat = deli(x, y)
            operacija = f"{x} / {y} = {rezultat}"

        print(f"--> {operacija}")
        
        zgodovina.append(operacija)
        if len(zgodovina) > 3:
            zgodovina.pop(0)
    else:
        print("Neveljavna izbira.")
