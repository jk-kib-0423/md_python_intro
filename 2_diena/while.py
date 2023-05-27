
"""
while <boolean loģika>:
    kods
    kas jaizpilda,
    ja boolean loģika ir true
    Jāparedz izeja

"""

sk1 = 5
sk2 = 10

# while sk1 < sk2:
#     print("Izpildās cikla 1 rindiņa")
#     print("Izpildās cikla 2 rindiņa")
#     print("Izpildās cikla 3 rindiņa")
#     sk1 = sk1 + 1

start = 55
stop = 75
step = 5

while start != stop:
    print(start)
    start = start + step


# break - apturēt cikla darbību un iziet ārā
# continue - pārlēkt pie nākamās iterācijas

print("================================================")
start = 55
stop = 75

while True:
    print("Šodien lielais hokejs!")
    if start >= stop:
        break
    
    start = start + 3