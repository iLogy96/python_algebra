cars = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ',2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}

# HEADER TABLE ROW
header_top_line = f'ID\tTip\t\tProizvodac\t\tRegistarska\t\tGodina prve\t\tCijena\t\tStar\tSkup'
header_bottom_line = f'  \t   \t\t          \t\toznaka\t\t\tregistracije\t\t(EUR)'
header_under_line = '_' * 125
print(header_top_line, '\n', header_bottom_line, '\n', header_under_line)

current_year = 2023

# BODY TABLE ROWs
for key, value in cars.items():
    # key = 1
    # value = ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    print(f'{key}', end='\t')     # Ispišemo ključ, ali ne pređeno u novi red nego dodamo TAB
    for element in value:      # Svaka vrijednost je jedna lista pa je onda tako i tretiramo
        # element = "Kamion"
        print(f'{element}', end='\t\t') # Ispišemo svaki element liste "vrijednost" i na kraju umjesto novog reda dodamo TAB
    
    manufacture_year = value[3]
    if ((current_year - manufacture_year) > 10):
        print("DA", end="\t")
    else:
        print("NE", end="\t")
    
    price = value[4]
    if (price > 10000):
        print("DA")
    else:
        print("NE", end="\n")
