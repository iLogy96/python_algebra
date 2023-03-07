cars = {
    0: ["Hatchback", "Citroen", "ZG1212ZG", 2022, 20000],
    1: ["Limousine", "Peugeot", "ZD1212ZD", 2022, 20000],
}

0 #FIFO , 2,3,4,5,6, 1 # LIFO

print(cars)

# cars.clear()
# print(cars)

# pop
# cars.pop(1)
print(cars)

# popitem
# LIFO - last-in first-out
# FIFO - first-in first-out
# print(cars.popitem())

# update
new_cars = {
    99: ["Racing car", "Maseratti", "DU1212DU", 300000]
}

print()
cars.update(new_cars)
print(cars)
