# Darbs ar failiem

faila_nosaukums = "dati.txt"

# režīmi: r - lasīšana, w - rakstīšana (pārraksta izdzēšot saturu), a - pievieno faila galā
with open(faila_nosaukums, "w", encoding="utf-8") as fails:
    fails.write("Pirmā testa rindiņa.\n")
    fails.write("Otra testa rindiņa.\n")


with open(faila_nosaukums, "a", encoding="utf-8") as fails:
    fails.write("Trešā rindiņa, kā papildinājums.\n")
    fails.write("Ceturtā rindiņa, nu jau lēnām pietiek.\n")


iepirkumi = ["sviests", "piens", "biezpiens", "krejums", "olas"]

# nav forši likt speciāli klāt jaunu rindu
iepirkumi2 = ["sviests\n", "piens\n", "biezpiens\n", "krejums\n", "olas\n"]

#print("\n".join(iepirkumi))

with open(faila_nosaukums, "a", encoding="utf-8") as fails:
    fails.write("\n".join(iepirkumi))
    fails.write("\n")
    # for prece in iepirkumi:
    #     fails.write(f"{prece}\n")
    
    #fails.writelines(iepirkumi2)


##################### Lasīt no faila ######################

# Ielasīt visu failu, kā vienu lielu simbola virkni
with open(faila_nosaukums, "r", encoding="utf-8") as fails:
    teksts = fails.read()

print(teksts)


with open(faila_nosaukums, "r", encoding="utf-8") as fails:
    rindinas = fails.readlines()
    for rindina in rindinas:
        print("+++", rindina, end="")