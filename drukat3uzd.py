def lasit_faila_rindas(fails):
    try:
        with open(fails, 'r') as f:
            rindas = f.readlines()
            if len(rindas) >= 4:
                print("Trešā rinda:", rindas[2])
                print("Ceturtā rinda:", rindas[3])
            else:
                print("Failā nav pietiekami daudz rindu!")
    except FileNotFoundError:
        print("Fails nav atrasts!")
    except IOError:
        print("Kļūda, nolasot failu!")

# Ievadiet faila nosaukumu
faila_nosaukums = input("Ievadiet faila nosaukumu: ")

lasit_faila_rindas(faila_nosaukums)