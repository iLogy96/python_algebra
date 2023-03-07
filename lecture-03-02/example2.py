# immutable - podatci se NE MOGU mijenjati
# mutable - podatci se MOGU mijenjati
# tuple
data = ("Python", "Algebra", "Python", "Coding")
print(data)

for entry in data:
    print(entry) # end="\n"

print(data[0])

# index
print(data.index("Python"))
print()

# count - broj pojavljivanja
print(data.count("Algebra"))
print(data.count("Python"))

lista_s_tupleom = [data]
lista_s_tupleom.append(2)
