# for cikls

print("=================================")
for i in range(10):
    print(i, end=", ")

print()
print("=================================")
# range(start, stop, step)
for i in range(15, 50):
    print(i, end=", ")


print()
print("=================================")
# range(start, stop, step)
for i in range(66, 99, 3):
    print(i, end=", ")

print()
print("=================================")
# range(start, stop, step)
for i in range(80, 20, -2):
    print(i, end=", ")


print()
print("=================================")
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    
    print()


iepirkumi = ["sviests", "piens", "biezpiens", "krejums", "olas"]

for i in range(len(iepirkumi)):
    print(iepirkumi[i])

