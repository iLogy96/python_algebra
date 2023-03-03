numbers = []

for num in range(20+1):
    numbers.append(num)

print(f"Old list: {numbers}")
# numbers.clear()
print(numbers)

# copy
new_numbers = numbers.copy()
# new_numbers = numbers
numbers.clear()

print(f"After copy:")
print(f"Old numbers: {numbers}") # empty output
print(f"new_numbers: {new_numbers}") # 
