def lasit (faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Failu '{faila_nosaukums}' nevarēja atrast.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

faila_nosaukums = 'sodien.txt'

lasit (faila_nosaukums)