# kreirati listu od 1 do broja 30
# ispisati sve brojeve koji su djeljivi s 3, 6, 9

# lista = [1 - 30]
# NOTE: iterirati ćemo po elementima liste
# for broj in lista:
# * je li broj djeljiv s 3, 6, 9
# * je li 15 djeljiv s 3?
# * 15 % 3 = 0
# * 16 % 3 = 1
# * 17 % 3 = 2
# * 18 % 3 = 0
# * 19 % 3 = 1
# * 20 % 3 = 2
#   je li broj djeljiv s 3
#   if (broj % 3 == 0):
#     ispiši broj

numbers = [1,2,3,4,5,6,7,8,9,10,31]
numbers = list(range(1,31))

numbers = []
for i in range(): #dodavanje u praznu listu
    numbers.append(i)

print(numbers)

for broj in numbers:
    # number is divisible by 3, 6 and 9
    if ((broj % 3 == 0) and (broj % 6 == 0) and (broj % 9 == 0)):
        print(f"Number {broj} is divisible by 3, 6 and 9")
