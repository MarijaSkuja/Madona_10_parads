def fails(fails):
    try:
        with open(fails, 'r') as f:
            saturs = f.read()
            print(saturs)
    except FileNotFoundError:
        print("Fails nav atrasts!")

# Ievadiet faila nosaukumu
faila_nosaukums = input("rinda.txt")
fails(faila_nosaukums)