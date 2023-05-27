"""
    ==      - salīdzināšanas operators, vai ir vienāds
    !=      - vai nav vienāds
    <       - mazāks par
    >       - lielāks par
    <=      - mazāks vai vienāds
    >=      - lielāks vai vienāds
"""

sk1 = 13
sk2 = 7
sk3 = 7

print("==============================")
print("sk1 == sk2:", sk1 == sk2)
print("sk1 != sk2:", sk1 != sk2)
print("sk1 < sk2:", sk1 < sk2)
print("sk1 > sk2:", sk1 > sk2)
print("sk1 <= sk2:", sk1 <= sk2)
print("sk1 >= sk2:", sk1 >= sk2)

print("==============================")
print("sk3 == sk2:", sk3 == sk2)
print("sk3 != sk2:", sk3 != sk2)
print("sk3 < sk2:", sk3 < sk2)
print("sk3 > sk2:", sk3 > sk2)
print("sk3 <= sk2:", sk3 <= sk2)
print("sk3 >= sk2:", sk3 >= sk2)



print("==============================")
vards1 = "Maris"
vards2 = "maris"
vards3 = "maris"
vards4 = "MariS"

print("Maris == maris:", vards1 == vards2)
print("maris == maris:", vards2 == vards3)

print("visi mazie burti salidzinasana", vards1.lower() == vards2.lower())
print("visi mazie burti salidzinasana", vards1.casefold() == vards2.casefold())

print("==============================")
patiesiba = True
meli = False

print("patiesiba == meli:", patiesiba == meli)
print("patiesiba != meli:", patiesiba != meli)


# AND, OR, NOT(!) operatori
"""
AND - skatās vai abas puses ir True
OR - vai kāda no pusēm ir True
! - apgriež otrādāk loģiku


A       B          A and B      A or B      A == B      !A
True    True        True        True        True        False
True    False       False       True        False       False
False   True        False       True        False       True 
False   False       False       False       True        True
"""

sk1 = 1
sk2 = 2
sk3 = 3
sk4 = 3
#                           True     and     True   ==> True
print("Rezultats AND1:", (sk2 > sk1) and (sk3 == sk4))
#                           False    and     True   ==> False
print("Rezultats AND2:", (sk2 < sk1) and (sk3 == sk4))
#                           True     or      True   ==> True
print("Rezultats OR1:",  (sk2 > sk1) or (sk3 == sk4))
#                           False    or      True   ==> True
print("Rezultats OR2:",  (sk2 < sk1) or (sk3 == sk4))

# Vai skaitlis ir intervālā no 3 - 5
sk1 >= 3 and sk1 <= 5
