def ierakstit(fails_nosaukums, vards):
    try:
        with open(fails_nosaukums, 'a') as fails:
            fails.write(vards + '\n')
        print(f"Vārds '{vards}' veiksmīgi ierakstīts failā '{fails_nosaukums}'.")
    except FileNotFoundError:
        print(f"Failu '{fails_nosaukums}' nevarēja atrast.")
    except PermissionError:
        print(f"Ierakstīšanas atļaujas trūkst failam '{fails_nosaukums}'.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

lietotaja_vards = input("Ievadiet savu vārdu: ")

fails_nosaukums = "lietotajs.txt"

ierakstit(fails_nosaukums, lietotaja_vards)