# Kreirajmo potrebne varijable za jedan racun
racun_broj = 'R-1-2021-01'
racun_datum_izdavanja = '31.02.2021'
# Stavke mogu biti rječnik čiji je key naziv proizvoda, a value je cijena
racun_stavke = {'Laptop':7.99,
                'Torba za laptop':4.99,
                'Monitor': 5.55,
                'Python za pocetnike': 5.55}
popusti = {'Laptop': 0}
# Izračunajmo koliki je ukupni iznos računa
racun_ukupan_iznos = 0
for stavka in racun_stavke.values():
    racun_ukupan_iznos += stavka
# Izračunajmo koliki je iznos PDV-a
racun_iznos_pdv = racun_ukupan_iznos * 0.25
popust = 0.2 # 20%

# Ispis racuna
print('\n\n')
print('*' * 50)
print(f'\n\tRACUN:\t\t{racun_broj}')
print(f'\tDATUM:\t\t{racun_datum_izdavanja}\n')
print('-' * 50)
print('\n\tProizvod\t\tCijena')
for proizvod, cijena in racun_stavke.items():
    if len(proizvod) < 10:
        print(f'\t{proizvod}\t\t\t{cijena} kn')
    elif len(proizvod) < 18:
        print(f'\t{proizvod}\t\t{cijena} kn')
    else :
        print(f'\t{proizvod}\t{cijena} kn')

print('\n')
print('-' * 50)
print(f'\n\tIZNOS PDV-a:\t{racun_iznos_pdv:.2f}')
print(f'\tUKUPAN IZNOS:\t{racun_ukupan_iznos:.2f}\n')
print(f'\n\tIZNOS popusta:\t{racun_ukupan_iznos * popust}')
print('*' * 50)
print('\n\n')