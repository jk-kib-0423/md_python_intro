"""
if <boolean loģika>:
    komandas
    vai vairakas
    kas javeic, ja rezultāts ir True
else:
    komandas
    vai vairakas
    kas javeic, ja rezultāts ir False
--------------------------------------------------------------------------
if <boolean loģika>:
    komandas
    vai vairakas
    kas javeic, ja rezultāts ir True
--------------------------------------------------------------------------
if <boolean loģika>:
    komandas
    vai vairakas
    kas javeic, ja rezultāts ir True
elif <boolean loģika>:
    komandas
    vai vairakas
    kas javeic, ja rezultāts ir True
elif <boolean loģika>:
    komandas
    vai vairakas
    kas javeic, ja rezultāts ir True
else: # šis nav obligāts
    komandas
    vai vairakas
    kas javeic, ja visi rezultāti ir False

if kaut_kas:
    komandas
else:
    if kaut_kas:
        komandas
    else:
        if kaut_kas:
            komandas
        
if kaut_kas:
    komandas
elif kaut_kas:
    komandas
elif kaut_kas:
    komandas    
"""


vecums = int(input("Cik tev ir gadu?"))

if vecums >= 18:
    print("Tu esi pilngadīgs!")
    print("Tu vari doties tālāk!")
else:
    print("Tu neesi pilngadīgs!")
    print("Tev ir nepieciešama vecāku atļauja.")

if vecums >= 65:
    print("Tu esi pensionārs.")

# Šeit ir kļūda loģikā (secīgums)
# if vecums < 50:
#     print("Piektā desmitgade")
# elif vecums < 40:
#     print("Ceturtā desmitgade")
# elif vecums < 30:
#     print("Trešā desmitgade")
# elif vecums < 20:
#     print("Otrā desmitgade")
# elif vecums < 10:
#     print("Pirmā desmitgade")
# else:
#     print("Tālāk vairs neskaitām!")

if vecums < 10:
    print("Pirmā desmitgade")
elif vecums < 20:
    print("Otrā desmitgade")
elif vecums < 30:
    print("Trešā desmitgade")
elif vecums < 40:
    print("Ceturtā desmitgade")
elif vecums < 50:
    print("Piektā desmitgade")
else:
    print("Tālāk vairs neskaitām!")


dz_gads = 1999
sis_gads = 2023
if sis_gads - dz_gads >= 18:
    print("Persona pilngadiga")




if vecums < 10:
    print("Pirmā desmitgade")
else:
    if vecums < 20:
        print("Otrā desmitgade")
    else:
        if vecums < 30:
            print("Trešā desmitgade")
        else:
            print("Utt......")