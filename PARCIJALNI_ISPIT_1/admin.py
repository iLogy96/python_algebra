from datetime import datetime

admins = [
    {
        "ime": "Adam",
        "prezime": "Random",
        "username": "Admin",
        "password": "1234567890",
    },
]
users = [
    {
        "ime": "Zdravko",
        "prezime": "Dren",
        "username": "ZZTop",
        "password": "1234567890",
    },
    {
        "ime": "Ivek",
        "prezime": "Blabla",
        "username": "Ivek123",
        "password": "abdefghijkl",
    },
]

# TODO edit feature for users and format interactive console


def LoginApp():
    while True:
        first_menu()
        choice = input("Choose wisely: ")

        if choice == "1":
            username = input("Unesi username od Admina: ")
            admin = check_user_or_admin(username, admins)

            if admin:
                print(
                    f"Logged in successfully, welcome {admin['ime']} {admin['prezime']}"
                )

                while True:
                    admin_menu()
                    sub_choice_admin = input("Choose wisely: ")

                    if sub_choice_admin == "1":
                        print(users)
                        user_deletion_choice = input("Kojeg usera želite izbrisati: ")
                        delete_user(user_deletion_choice)

                    elif sub_choice_admin == "2":
                        create_user()
                        print(f"Current user(s): {users}")

                    elif sub_choice_admin == "3":
                        break
            else:
                print("Ovo nisu točni podaci za admina")

        if choice == "2":
            while True:
                user_menu()
                sub_choice_user = input("Choose wisely: ")

                if sub_choice_user == "1":
                    create_user()

                elif sub_choice_user == "2":
                    print("Login with your username and password")
                    username = input("Enter your username: ")
                    user = check_user_or_admin(username, users)

                    if user:
                        print(
                            f"Logged in successfully, welcome {user['ime']} {user['prezime']}"
                        )
                        while True:
                            edit_user_menu(user)
                            sub_choice_edit = input("Choose wisely: ")

                            if sub_choice_edit == "1":
                                return
                            elif sub_choice_edit == "2":
                                break

                elif sub_choice_user == "3":
                    break

        elif choice == "3":
            print("Hvala što ste koristili LoginApp")
            break


# note to self snake case
# Menus:
def first_menu():
    print("Welcome to LoginApp, choose an option")
    print("1.Izbornik za admina")
    print("2.Izbornik za korisnike")
    print("3.Exit app")


def user_menu():
    print("1.Register")
    print("2.Login")
    print("3.Return")


def edit_user_menu(user):
    print(f"Current user: {user['ime']} {user['prezime']}")
    print("1.Edit User")
    print("2.Return")
    print(datetime.now().strftime("%Y/%m/%d %H:%M"))


def admin_menu():
    print("1.Remove user")
    print("2.Add user")
    print("3.Return")


# Methods:
def check_user_or_admin(username, list):
    for user in list:
        if username == user["username"]:
            password = input("Unesi password: ")
            if password == user["password"]:
                return user
            else:
                print("Unijeli ste krivi password")
                break
    else:
        print("User doesn't exist")


# def edit_user(user):



def create_user():
    name = input("Create name: ")
    surname = input("Create surname: ")
    username = input("Create username: ")
    password = input("Enter password at least 10 characters long: ")
    if len(password) >= 10:
        users.append(
            {
                "ime": name,
                "prezime": surname,
                "username": username,
                "password": password,
            }
        )
        print("User created successfully")
    else:
        print("Password does not meet requirements")


def delete_user(username):
    for user in users:
        if username == user["username"]:
            users.remove(user)
            print(f"Uspješno ste izbrisali usera {user['username']}")
            print(f"Preostali useri su {users}")
            break
    else:
        print("Taj user ne postoji")


LoginApp()
