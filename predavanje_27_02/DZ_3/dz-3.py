from tabulate import tabulate

vozilaFirme = [
    [0, "Gallardo", "Lamborđini", "ZG1234-BK", "2017", "100 000 Eur"],
    [
        1,
        "M3",
        "BMW",
        "DA1234-BK",
        "2012",
        "50 000 Eur",
    ],
    [
        2,
        "WRX STI",
        "Subaru",
        "VZ1234-BK",
        "2008",
        "35 000 Eur",
    ],
]

print(
    tabulate(
        vozilaFirme,
        headers=[
            "ID",
            "Tip auta",
            "Proizvodnja",
            "Registracija",
            "Godina prve registracije",
            "Cijena u EUR",
        ],
        tablefmt="fancy_grid",
    )
)
