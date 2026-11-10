# Bloomie on virtuaalne õppeaed, kus kasutaja saab lisada õppeaineid ja ülesandeid.
# Ülesannete täitmisel kasvavad virtuaalsed lilled.

# Programmi käivitamine:
# 1. Laadi projekt GitHubist alla.
# 2. Ava fail main.py Thonnys.
# 3. Käivita programm (F5).
# 4. Vali menüüst sobiv tegevus ja järgi juhiseid.
# Programmi kasutamiseks peavad failid main.py, tasks.py ja aed.py olema samas kaustas.

# Autorid: Varvara Gavrilova ja Elmira Rafiyeva


# Impordime funktsioonid teistest failidest
from tasks import lisa_aine, lisa_ülesanne, vaata_ülesandeid, märgi_tehtuks
from aed import vaata_aeda


def main():
    
    ained = {} # Loob tühja sõnastiku õppeainete jaoks
    
    while True:
        
        print("\n--- BLOOMIE ---")
        print("1. Lisa õppeaine")
        print("2. Lisa ülesanne")
        print("3. Vaata ülesandeid")
        print("4. Märgi ülesanne tehtuks")
        print("5. Vaata aeda")
        print("0. Välju")

        
        valik = input("Tee valik: ")

        
        if valik == "1":
            lisa_aine(ained)

        elif valik == "2":
            lisa_ülesanne(ained)

        elif valik == "3":
            vaata_ülesandeid(ained)

        elif valik == "4":
            märgi_tehtuks(ained)

        elif valik == "5":
            vaata_aeda(ained)

        elif valik == "0":
            print("Head aega!")
            break

        else:
            print("Vale valik. Proovi uuesti.")



if __name__ == "__main__":
    main()


