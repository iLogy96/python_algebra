# Write a Python program to get the frequency of elements in a
# given list of lists. (try with multiple level nested lists)

listOfLists = [
    "A",
    "A",
    "A",
    ["A", "B", "C"],
    "B",
    ["B", "C", "D"],
    "C",
    ["C", "D", "E"],
]
frequency = {}

for item in listOfLists:
    if len(item) > 1:
        for nestedItem in item:
            if nestedItem in frequency:
                frequency[nestedItem] += 1
            else:
                frequency[nestedItem] = 1
    else:
        if item in frequency.keys():
            frequency[item] += 1
        else:
            frequency[item] = 1

print(frequency)
