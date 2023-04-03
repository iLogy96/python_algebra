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
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

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

# Interaktivna konzola:
while True:
    print(f"Dobrodošli u sučelje banke: {bank.name}, molimo izaberite opciju")
    print(
        "1.Izradite račun\n2.Uđite u već postojeći račun\n3.Zatvorite postojeći račun\n4.Ugasite aplikaciju\n"
    )

    choice = input("Izaberite opciju: ")

    if choice == "1":
        id = input("Unesite jedinstveni broj računa: ")
        ime = input("Unesite ime vlasnika računa: ")
        svota = float(input("Unesite svotu eura s kojom raspolažete: "))
        account = Account(id, ime, svota)
        bank.add_account(account)
        print("Uspješno ste izradili račun\n")

    elif choice == "2":
        id = input("Unesite jedinstveni broj računa kako bi ga mogli pronaći: ")
        account = bank.get_account(id)
        if account is None:
            print("Račun ne postoji...Molim vas izradite ga prvo")
        else:
            print(
                "Račun pronađen...Odaberite opciju\n1.Uplata\n2.Isplata\n3.Provjera stanja računa"
            )

            pod_izbor = input("Unesite opciju: ")

            if pod_izbor == "1":
                amount = float(input("Unesite svotu za uplatu: "))
                account.deposit(amount)
                print(
                    f"Transakcija uspješna, trenutno stanje računa je {account.balance}\n"
                )

            elif pod_izbor == "2":
                amount = float(input("Unesite svotu za isplatu: "))
                account.withdraw(amount)
                print(
                    f"Transakcija uspješna, trenutno stanje računa je {account.balance}\n"
                )
            elif pod_izbor == "3":
                print(f"Stanje računa je {account.balance}\n")
            else:
                print("Krivi unos\n")

    elif choice == "3":
        id = input("Unesite broj računa koji želite zatvoriti\n")
        account = bank.get_account(id)
        if account is None:
            print("Račun ne postoji...Molim vas izradite ga prvo\n")
        else:
            bank.remove_account(account)
            print("Uspješno ste izbrisali račun\n")

    elif choice == "4":
        print("Thank you for using", bank.name)
        break

    else:
        print("Opcija je kriva ili ne postoji")
