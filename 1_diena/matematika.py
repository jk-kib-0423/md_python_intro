import math

sk1 = 5
sk2 = 3

print(f"sk1={sk1}, sk2={sk2}")

print(sk1 + sk2)
print(sk1, "+", sk2, "=", sk1 + sk2)
print(f"{sk1} + {sk2} = {sk1 + sk2}")

rezultats = sk1 + sk2

print("Rezultats:", rezultats)

print(f"{sk1} - {sk2} = {sk1 - sk2}")
print(f"{sk1} * {sk2} = {sk1 * sk2}")
print(f"{sk1} / {sk2} = {sk1 / sk2}")

sk1 = 13
sk2 = 5
print(f"{sk1} / {sk2} = {sk1 / sk2}")
print(f"{sk1} // {sk2} = {sk1 // sk2}") # Dalīt ar rezultātā veselu skaitli

# Modulis - nesadalītā daļa - atlikums
print(f"{sk1} % {sk2} = {sk1 % sk2}")
# 13 // 5 = 2
# 2 * 5 = 10
# 13 - 10 = 3 <---

print(f"{sk1} ** 2 = {sk1 ** 2}") # Kāpināšana

print("========================================")
sk1 = 5
sk2 = 3
cipari_aiz_komata = 4
apalots = sk1 / sk2
apalots = round(apalots, cipari_aiz_komata)
print("Apaļošanas rezultāts:", apalots)

print("Apaļošanas rezultāts:", round(sk1 / sk2, cipari_aiz_komata))
print("========================================")

malaA = 5
malaB = 4
laukums = malaA * malaB
print("Laukums:", laukums)

print(math.pi)
