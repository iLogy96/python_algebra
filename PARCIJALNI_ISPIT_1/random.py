users = []


def createUser(ime, prezime, username, password):
    if username in users:
        return username
    else:
        users.append(
            {
                "name": ime,
                "surname": prezime,
                "username": username,
                "password": password,
            }
        )
    print(users)


def checkExistingUser(username):
    for user in users:
        if user in users:
            print(f"User {username} found, please enter correct password: \n")
            password = input("Password: ")
            print(user[password])
            if password == user[password]:
                print(f"Password entered correctly, welcome user {username}\n")
            else:
                print("Password doesn't match this account\n")
        else:
            print("Username not found\n")


def login():
    while True:
        print("Welcome to Login, do you have an account or do you need to register ?")
        print("1.Register\n2.Enter credentials for existing account\n3.Exit app\n")

        choice = input("Choose wisely: \n")

        if choice == "1":
            print("Create name: \n")
            name = input("Name: ")
            print("Create surname: \n")
            surname = input("Surname: ")
            print("Create username: \n")
            username = input("Username: ")
            print("Create password at least 10 characters long: \n")
            password = input("Password: ")
            if len(password) >= 10:
                createUser(name, surname, username, password)
                print(f"User {name},{surname} successfully created\n")
            else:
                print("Password not long enough, please try again\n")

        elif choice == "2":
            print("Enter your credentials please\n")
            username = input("Username: ")
            checkExistingUser(username)

        elif choice == "3":
            print("Thanks for using login app")
            break


login()
