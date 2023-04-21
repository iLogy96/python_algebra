class Račun:
    def __init__(self, racun_broj, racun_datum_izdavanja):
        self.racun_broj = racun_broj
        self.racun_datum_izdavanja = racun_datum_izdavanja
        self.racun_stavke = {
            "Laptop": 7.99,
            "Torba za laptop": 4.99,
            "Monitor": 5.55,
            "Python za pocetnike": 5.55,
        }
        self.racun_ukupan_iznos = 0
        self.racun_iznos_pdv = 0
        self.popust = 0.2

    def izračun_ukupnog_iznosa(self):
        for stavka in self.racun_stavke.values():
            self.racun_ukupan_iznos += stavka

    def izračun_PDV(self):
        self.racun_iznos_pdv = self.racun_ukupan_iznos * 0.25

    def ispis(self):
        self.izračun_ukupnog_iznosa()
        self.izračun_PDV()
        print("\n\n")
        print("*" * 50)
        print(f"\n\tRACUN:\t\t{self.racun_broj}")
        print(f"\tDATUM:\t\t{self.racun_datum_izdavanja}\n")
        print("-" * 50)
        print("\n\tProizvod\t\tCijena")
        for proizvod, cijena in self.racun_stavke.items():
            if len(proizvod) < 10:
                print(f"\t{proizvod}\t\t\t{cijena} kn")
            elif len(proizvod) < 18:
                print(f"\t{proizvod}\t\t{cijena} kn")
            else:
                print(f"\t{proizvod}\t{cijena} kn")
        print("\n")
        print("-" * 50)
        print(f"\n\tIZNOS PDV-a:\t{self.racun_iznos_pdv:.2f}")
        print(f"\tUKUPAN IZNOS:\t{self.racun_ukupan_iznos:.2f}\n")
        print(f"\n\tIZNOS popusta:\t{self.racun_ukupan_iznos * self.popust}")
        print("*" * 50)
        print("\n\n")


racun_broj = "R-1-2021-01"
racun_datum_izdavanja = "31.02.2021"
bill_1 = Račun(racun_broj, racun_datum_izdavanja)
bill_1.ispis()
