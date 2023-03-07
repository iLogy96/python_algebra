import datetime

vozilaFirme = {
    0: [
        "Gallardo",
        "Lamborđini",
        "ZG1234-BK",
        "2017",
        100000,
    ],
    1: [
        "M3",
        "BMW",
        "DA1234-BK",
        "2012",
        50000,
    ],
    2: [
        "WRX STI",
        "Subaru",
        "VZ1234-BK",
        "2008",
        35000,
    ],
}


print(
    "{:<8} {:<15} {:<15} {:<15} {:<25} {:<15} {:<10} {:<20}".format(
        "ID",
        "Tip auta",
        "Proizvodnja",
        "Registracija",
        "Godina prve registracije",
        "Cijena u EUR",
        "Star",
        "Skup",
    )
)

aktualnaGodina = 2023

for keys, values in vozilaFirme.items():
    ageCriteria = datetime.date.today().year - int(values[3]) > 10
    priceCriteria = values[4] > 40000

    if ageCriteria == True and priceCriteria == True:
        values = values + ["DA", "DA"]
    if ageCriteria == True and priceCriteria == False:
        values = values + ["DA", "NE"]
    if ageCriteria == False and priceCriteria == True:
        values = values + ["NE", "DA"]
    else:
        values = values + ["NE", "NE"]
    print(
        "{:<8} {:<15} {:<15} {:<15} {:<25} {:<15} {:<10} {:<20}".format(keys, *values)
    )
