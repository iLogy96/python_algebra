vozilaFirme = {
    0: [
        "Gallardo",
        "Lamborđini",
        "ZG1234-BK",
        "2017",
        "100 000 Eur",
    ],
    1: [
        "M3",
        "BMW",
        "DA1234-BK",
        "2012",
        "50 000 Eur",
    ],
    2: [
        "WRX STI",
        "Subaru",
        "VZ1234-BK",
        "2008",
        "35 000 Eur",
    ],
}


print(
    "{:<8} {:<15} {:<15} {:<15} {:<25} {:<15}".format(
        "ID",
        "Tip auta",
        "Proizvodnja",
        "Registracija",
        "Godina prve registracije",
        "Cijena u EUR",
    )
)

for keys, values in vozilaFirme.items():
    print("{:<8} {:<15} {:<15} {:<15} {:<25} {:<15}".format(keys, *values))
