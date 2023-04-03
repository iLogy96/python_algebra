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


def LoginApp():
    while True:
        print("Welcome to LoginApp, choose an option")
        print("1.Register")
        print("2.Login")
        print("3.Exit app")

        choice = input("Choose wisely: ")

        if choice == "1":
            print("Create name: ")
            name = input("Enter name: ")
            print("Create surname: ")
            surname = input("Enter surname: ")
            print("Create username: ")
            username = input("Enter username: ")
            print("Create password at least 10 characters long: ")
            password = input("Enter password: ")
            if len(password) >= 10:
                createUser(name, surname, username, password)
                print("User created successfully")
            else:
                print("Password does not meet requirements")

        elif choice == "2":
            print("Login with your username and password")
            username = input("Enter your username: ")
            user = checkExistingUser(username)
            if user:
                print(
                    f"Logged in successfully, welcome {user['ime']} {user['prezime']}"
                )
        elif choice == "3":
            print("Hvala što ste koristili LoginApp")
            break


def checkExistingUser(username):
    for user in users:
        if username == user["username"]:
            password = input("Unesi password za usera: ")
            if password == user["password"]:
                return user
            else:
                print("Unijeli ste krivi password")
                break
    else:
        print("User doesn't exist")


def createUser(ime, prezime, username, password):
    users.append(
        {
            "ime": ime,
            "prezime": prezime,
            "username": username,
            "password": password,
        }
    )


LoginApp()
