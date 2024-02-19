def lasit (faila_nosaukums):
    try:
        # Atver failu norādītajā režīmā (lasīšana)
        with open(faila_nosaukums, 'r') as fails:
            # Nolasa faila saturu
            saturs = fails.read()

            # Izdrukā faila saturu
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Failu '{faila_nosaukums}' nevarēja atrast.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

# Norādiet faila nosaukumu, kuram vēlaties nolasīt saturu
faila_nosaukums = 'sodien.txt'

# Izsauc funkciju, padodot faila nosaukumu
lasit (faila_nosaukums)