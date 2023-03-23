# Palindrom check - using while loop

def isPalindrom(str):
    while str.lower() == str[::-1].lower():
        print(f"{str} je palindrom")
        break
    else:
        print(f"{str} nije palindrom")


isPalindrom("Anavolimilovana")
