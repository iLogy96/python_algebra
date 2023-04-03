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

# iteriraj dokle god range vraća broj 
for i in range(0,10):
    print(i)

counter = 0
while counter < 10:
    # pristupamo nekoj listi 
    print("condition is true")
    counter+=1


length = len(vozilaFirme.items()) # 3

# implicitan uvjet
# iteriraj dokle god postoji itema u dict
# for keys, values in vozilaFirme.items():
    
counter = 0
while counter < length:
    # 3 < 3 -> False
    # key = list(vozilaFirme.keys())[counter]
    keys = vozilaFirme.keys()
    keys = list(keys)
    key = keys[counter]
    values = vozilaFirme[key]

    tip, proizvodnja, rega, godinaRege, cijena = values
    print(
        "{:<8} {:<15} {:<15} {:<15} {:<25} {:<15}".format(
            key, tip, proizvodnja, rega, godinaRege, cijena
        )
    )
    counter+=1

print("Ispisano")
