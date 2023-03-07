"""                        *          +
A           B           A and B     A or B
True        Ture        True        True
True        False       False       True
False       True        False       True
False       False       False       False
"""
condition_1 = True
condition_2 = True
condition_3 = True

# if (condition_1 == True): firstly, the operator is resolved
if condition_1:
    print("Condition 1 is true")
    print()
# else if
elif condition_2:
    print("Condition 2 is true")
else:
    # print("Condition 1 is not true")
    print()
print("\n\n\n")


number = 63
locker = 9

if number < 50:
    print("Number is lesser than 50")
else:
    print("Number is greater than 50")

if locker <= 3:
    print("Locker is within the first 3 lockers")
else:
    print("Locker is NOT within the first 3 lockers")

result = ((number < 50) and (locker <= 3))
print(f"result: {result}")

# if ((number < 50) and (locker <= 3)):
# if ((True) and (True))
if (result):
    print("Number is lesser than 50 and Locker is within the first 3 lockers")
else:
    print("They're not")
    