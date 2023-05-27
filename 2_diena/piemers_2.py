import random

min = 1
max = 20
skaitlis = random.randint(min, max)
meginajumi = 0

# print("Gadījuma skaitlis ir:", skaitlis)

print(f"Minēšanas spēle! Atmini skaitli intervālā no {min} - {max}")

while True:
    minejums = int(input("Ievadi skaitli, kuru gribi uzminēt:"))
    meginajumi = meginajumi + 1
    
    if minejums == skaitlis:
        print("Apsveicam ar uzvaru - skaitlis ir uzminēts!")
        print(f"Lai uzvarētu tev tas prasīja {meginajumi} reizes.")
        break
    else:
        # Papildus informāicija leitotājam
        if minejums > skaitlis:
            print("Tavs minējums ir par augstu!")
        else:
            print("Tavs minējums ir par zemu.")