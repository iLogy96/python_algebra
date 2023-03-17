# str1 = input("Unesi prvi string: ").split()
# str2 = input("Unesi drugi string: ").split()

# A = set(str1)
# B = set(str2)

# print(A.symmetric_difference(B))

str1 = input("Unesi prvi string: ")
str2 = input("Unesi drugi string: ")

similarLetters = []
differentLetters = []

for i in str1.lower():
    for j in str2.lower():
        if i == j:
            similarLetters.append(i)
            break
print(similarLetters)
