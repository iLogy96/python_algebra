import os
from datetime import datetime


class BankingApp:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def get_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def get_total_balance(self):
        total_balance = 0
        for acc in self.accounts:
            total_balance += acc.balance
        return total_balance


class Account:
    def __init__(
        self, account_number, balance, company_name, name, surname, address, city
    ):
        self.account_number = account_number
        self.name = name
        self.surname = surname
        self.balance = balance
        self.company_name = company_name
        self.address = address
        self.city = city

    def deposit(self, deposited_amount):
        if deposited_amount > 0:
            self.balance += deposited_amount
        else:
            print("Pogrešan unos")

    def withdraw(self, withdrawn_amount):
        if withdrawn_amount > self.balance:
            ("Nemate toliko novaca")
        else:
            self.balance -= withdrawn_amount


# Initialization
bank = BankingApp("KraDeZe")
randomAcc1 = Account(
    "12345678911",
    2000,
    "Tvrtkica",
    "Tvrtko",
    "Tvrtkić",
    "Maksimirska 125",
    "Zagreb",
)
randomAcc2 = Account(
    "11395658912",
    55000,
    "Random123",
    "Ivan",
    "Horvat",
    "Horvatovac 11b",
    "Zagreb",
)
bank.add_account(randomAcc1)
bank.add_account(randomAcc2)

# Interaktivna konzola:
while True:
    print(f"Dobrodošli u sučelje banke: {bank.name}, molimo izaberite opciju")
    print(
        "1.Izradite račun\n2.Uđite u već postojeći račun\n3.Zatvorite postojeći račun\n4.Ugasite aplikaciju\n"
    )

    choice = input("Izaberite opciju: ")

    if choice == "1":
        id = input("Unesite jedinstveni broj računa (OIB): ")
        if len(id) < 11 or len(id) > 11:
            print("OIB je predug ili prekratak, mora imati TOČNO 11 znakova")
        else:
            company_name = input("Unesite ime tvrtke: ")
            name = input("Unesite ime vlasnika računa: ")
            surname = input("Unesite prezime vlasnika računa: ")
            address = input("Unesite adresu tvrtke: ")
            city = input("Unesite grad u kojoj se nalazi tvrtka: ")
            balance = float(input("Unesite svotu eura s kojom raspolažete: "))
            account = Account(id, balance, company_name, name, surname, address, city)
            bank.add_account(account)
            os.system("cls" if os.name == "nt" else "clear")
            print(
                f"Uspješno ste izradili račun...\nDobrodošli korisnik BA-{datetime.now().strftime('%Y-%m')}-{str(len(bank.accounts)).zfill(5)}"
            )

    elif choice == "2":
        id = input("Unesite jedinstveni broj računa kako bi ga mogli pronaći: ")
        account = bank.get_account(id)
        if account is None:
            os.system("cls" if os.name == "nt" else "clear")
            print("Račun ne postoji...Molim vas izradite ga prvo")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                # os.system("cls" if os.name == "nt" else "clear")
                print(
                    f"Račun pronađen...Dobrodošli BA-{datetime.now().strftime('%Y-%m')}-{str(len(bank.accounts)).zfill(5)}\nOdaberite opciju\n1.Uplata\n2.Isplata\n3.Provjera stanja računa\n4.Nazad na prethodni izbornik"
                )

                pod_izbor = input("Unesite opciju: ")

                if pod_izbor == "1":
                    amount = float(input("Unesite svotu za uplatu: "))
                    account.deposit(amount)
                    os.system("cls" if os.name == "nt" else "clear")
                    print(
                        f"Transakcija uspješna, trenutno stanje računa je {account.balance} EUR({account.balance*7.5}HRK)\n"
                    )

                elif pod_izbor == "2":
                    amount = float(input("Unesite svotu za isplatu: "))
                    account.withdraw(amount)
                    os.system("cls" if os.name == "nt" else "clear")
                    print(
                        f"Transakcija uspješna, trenutno stanje računa je {account.balance} EUR({account.balance*7.5}HRK)\n"
                    )
                elif pod_izbor == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(
                        f"Stanje računa je {account.balance} EUR({account.balance*7.5}HRK)\n"
                    )
                elif pod_izbor == "4":
                    os.system("cls" if os.name == "nt" else "clear")
                    break

                else:
                    print("Krivi unos\n")
    elif choice == "3":
        id = input("Unesite broj računa koji želite zatvoriti\n")
        account = bank.get_account(id)
        if account is None:
            os.system("cls" if os.name == "nt" else "clear")
            print("Račun ne postoji...Molim vas izradite ga prvo\n")
        else:
            bank.remove_account(account)
            os.system("cls" if os.name == "nt" else "clear")
            print("Uspješno ste izbrisali račun\n")

    elif choice == "4":
        os.system("cls" if os.name == "nt" else "clear")
        print("Thank you for using", bank.name)
        break

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Opcija je kriva ili ne postoji")
