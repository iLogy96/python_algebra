str1 = input("Unesi string: ")

if len(str1) % 4 == 0:
    print(str1[::-1])
else:
    print("String nije djeljiv s 4")
