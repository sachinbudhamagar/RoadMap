# Json database
users = {
    "sachin": "Sachin1",
    "admin": "admin123",
}
max_attempts = 3


def login():

    attempts = 0
    print("\n==========>Login System<===========")
    print("Type q to quit program\n")

    while attempts < max_attempts:
        try:
            name = input("Enter username: ").strip()
            if name == "q":
                print("Exiting program..")
                return None

            if name == "":
                print("Name cannot be empty! try again")
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"{remaining} attempts left")
                continue

            if name not in users:
                print("Invalid username! Try again")
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"{remaining} attempts left")
                continue

            word = input("Enter password: ").strip()

            if word == "":
                print("Password cannot be empty!")
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"{remaining} attempts left")
                attempts += 1
                continue

            if word not in users[name]:
                print("Invalid password! try again")
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"{remaining} attempts left")
                continue

            print(f"\nWelcome, {name}")
            return name

        except KeyboardInterrupt:
            print("\nExiting program")
            return None


if __name__ == "__main__":
    result = login()
    if result:
        print(f"\nLogged in as: {result}")
    else:
        print("\nFailed to login.")
