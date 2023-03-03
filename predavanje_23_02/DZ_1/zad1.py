# Domaća zadaća 1

carMileage = 5.3
gasPrice = 9.56
kilometersPassed = 100


def gasExpense(mileage, gas, kilometers):
    return gas * (kilometers / 100) * mileage


def gasExpensePerMonth(months):
    return gasExpense(carMileage, gasPrice, kilometersPassed) * months


print(gasExpense(5.3, 9.56, 100))
print(gasExpensePerMonth(2))
