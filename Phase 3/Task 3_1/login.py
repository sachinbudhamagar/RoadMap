username = ["Sachin"]
password = ["sachin1"]
max_attempts = 3
is_valid = True


def login():
    attempts = 0
    while attempts < max_attempts:
        try:
            name = input("Enter username: ").lower()
            if name.strip() == "q":
                print("Exiting program..")
                break

            if name.strip() == "":
                print("Name cannot be empty! try again")
                attempts += 1
                continue
            else:
                if is_valid:
                    if name in username:
                        word = input("Enter password: ").strip()
                        if word not in password:
                            print("Invalid password! try again")
                            attempts += 1
                            remaining = max_attempts - attempts
                            print(f"{remaining} attempt left")
                        else:
                            print("Welcome admin")
                            break

        except KeyboardInterrupt:
            print("\nExiting program")
            break


if __name__ == "__main__":
    result = login()
    print(result)
