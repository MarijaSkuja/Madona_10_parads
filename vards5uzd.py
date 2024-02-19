def ierakstit_vardu_faila(fails_nosaukums, vards):
    try:
        # Atver failu norādītajā režīmā (papildināšana)
        with open(fails_nosaukums, 'a') as fails:
            # Ieraksta lietotāja ievadīto vārdu failā
            fails.write(vards + '\n')
        print(f"Vārds '{vards}' veiksmīgi ierakstīts failā '{fails_nosaukums}'.")
    except FileNotFoundError:
        print(f"Failu '{fails_nosaukums}' nevarēja atrast.")
    except PermissionError:
        print(f"Ierakstīšanas atļaujas trūkst failam '{fails_nosaukums}'.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

# Lietotāja ievadītais vārds
lietotaja_vards = input("Ievadiet savu vārdu: ")

# Norādiet faila nosaukumu, kuram vēlaties ierakstīt vārdu
fails_nosaukums = "lietotajs.txt"

# Izsauc funkciju, padodot faila nosaukumu un lietotāja vārdu
ierakstit_vardu_faila(fails_nosaukums, lietotaja_vards)