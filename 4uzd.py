def failu(fails):
    try:
        with open(fails, 'r') as f:
            saturs = f.read()
            print(saturs)
    except FileNotFoundError:
        print("Fails nav atrasts!")
    except IOError:
        print("Kļūda, nolasot failu!")

# Ievadiet faila nosaukumu
faila_nosaukums = input("Ievadiet faila nosaukumu: ")
faila_formats = input("Ievadiet faila formātu (paplašinājumu): ")

faila_nosaukums_ar_formats = f"{faila_nosaukums}.{faila_formats}"

failu(faila_nosaukums_ar_formats)