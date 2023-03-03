numbers = [] 

for num in range(0, 20, 2): # [0,2,...]
    numbers.append(num)

print(f"Old list: {numbers}")

# count
# print(numbers.count(20))
numbers.append(20)
# print(numbers.count(20))

names = ["Ivan", "Ivan"]
print(names.count("Ivan"))

# extend
# names.extend(["Ivan", "Ivan", "Ivan"])
# names = names + ["Ivan", "Ivan", "Ivan"]
# names += ["Ivan", "Ivan", "Ivan"]

print(numbers)

# index
# print(numbers.index(14))

# insert
numbers.insert(-1, -10)
print(numbers)

# pop
numbers.pop()
print(numbers)

# reverse
numbers.reverse()
print(numbers)
numbers.reverse()
print(numbers)

# sort
numbers.sort(reverse=True)
print(numbers)
