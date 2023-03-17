# print first 5 and last 5 characters of given string

firstFive = []
lastFive = []


def printFive(string):
    for i in range(5):
        firstFive.append(string[i])
        lastFive.append(string[-i - 1])
    print(firstFive, lastFive[::-1])


printFive("JedanDvaTriČetiri")

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)

# Output: Reversed List: [7, 5, 3, 2]