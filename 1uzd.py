def lasit_failu(fails):
    try:
        with open(fails, 'r') as f:
            saturs = f.read()
            print(saturs)
    except FileNotFoundError:
        print("Fails nav atrasts!")

# Ievadiet faila nosaukumu
faila_nosaukums = input("rinda.txt")
lasit_failu(faila_nosaukums)