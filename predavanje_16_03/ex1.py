# Write a Python program to remove duplicate words from a given string.

def removeDuplicates(str):
    empty_set = set()
    for char in str.lower():
        empty_set.add(char)
    return empty_set


removeDuplicates("samo samo samo jednom")
