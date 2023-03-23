# tablica množenja

def multiplicationTable(number):
    i = 0
    while i <= number:
        print(f"{i} x {number} =", i * number)
        i += 1


multiplicationTable(5)
