# Domaća zadaća 2
def moneyReturned(money, years):
    earnedSum = 0

    for year in range(1, years + 1):
        bankRateReturn = round(money * 0.025, 2)
        earnedSum += bankRateReturn
        money = (money * 0.025) + money
        print(f"year {year} you earned {bankRateReturn}")

    print(f"Your total sum is {round(money,2)} and you earned {round(earnedSum,2)}")


moneyReturned(10000, 15)
