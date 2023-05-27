iepirkumi = ["sviests", "piens", "biezpiens", "krejums", "olas"]
skaitli = [1, 5, 3, 21, 4, 15, 16, 99, 22, 55, 43, -10, -5, 0]

print("=======================================")
for prece in iepirkumi:
    print(prece)

print("=======================================")
for skaitlis in skaitli:
    if skaitlis % 5 == 0:
        print("Atradu skaitli, kas dalās ar 5:", skaitlis)



print("=======================================")

para_skaitli = []
nepara_skaitli = []
for skaitlis in skaitli:
    if skaitlis % 2 == 0:
        print("Atradu pāra skaitli:", skaitlis)
        para_skaitli.append(skaitlis)
    else:
        print("Atradu NE-pāra skaitli:", skaitlis)
        nepara_skaitli.append(skaitlis)

para_skaitli.sort()
nepara_skaitli.sort()

print("Pāra skaitli", para_skaitli)
print("Nepāra skaitli", nepara_skaitli)

visi_skaitli = para_skaitli + nepara_skaitli

print("Visi skaitli", visi_skaitli)