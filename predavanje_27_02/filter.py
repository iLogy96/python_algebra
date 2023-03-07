lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

listOfWords = lorem.split(" ")

def findInstancesOfStr(str):
    counter = 0
    for i in range(len(listOfWords)):
        if listOfWords[i].startswith(str):
            counter += 1
    print(f"Your entered word is appearing {counter} times in the given text")


findInstancesOfStr("in")

#metoda count zamijeni sve ovo