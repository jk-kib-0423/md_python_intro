
# indeksi       0           1          2        3           4
iepirkumi = ["sviests", "piens", "biezpiens", "krejums", "olas"]

print(iepirkumi)

# Izdrukāt vienu konkrētu elementu ar attiecīgu indeksu
print(iepirkumi[1])
print(iepirkumi[3])

# Elementu pievienošana (saraksta beigās)
print("Pievienojam galā jogurtu:")
iepirkumi.append("jogurts")
print(iepirkumi)

# Elementu pievienošana konkrētā pozīcijā
print("Pievienojam 2 indeksā sieru:")
iepirkumi.insert(2, "siers")
print(iepirkumi)

# Izdzēstno saraksa konkrētu elementu
print("Izdzēšam pienu no saraksta:")
iepirkumi.remove("piens")
print(iepirkumi)

# Izdzēst pēdējo vai pēc indeksa
print("Izdzēšam pēdējo elementu no saraksta:")
iepirkumi.pop()
print(iepirkumi)

print("Izdzēšam konkrētu elementu no saraksta (3):")
iepirkumi.pop(3)
print(iepirkumi)

print("=======================================")
# Atrast konkrēta elementa indeksu
indeks = iepirkumi.index("olas")
print("Olas indeks:", indeks)



if "siers" in iepirkumi:
    iepirkumi.remove("siers")

if "udens" in iepirkumi:
    iepirkumi.remove("udens")
else:
    print("Udens saraksta nav, nevaru izdzest!")

print(iepirkumi)

iepirkumi.sort()

print(iepirkumi)

print("Sarakstā kopā ir", len(iepirkumi), "elementi!")
print("Pēdējais saraksta indeks ir", len(iepirkumi) - 1)


temp = iepirkumi[2]
iepirkumi[2] = iepirkumi[0]
iepirkumi[0] = temp

print(iepirkumi)

# a, b = b, a - samainit a un b vertības vietām
iepirkumi[0], iepirkumi[2] = iepirkumi[2], iepirkumi[0]

print(iepirkumi)



print("_#_".join(iepirkumi))