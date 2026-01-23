allowed_password = ["test"]
is_valid = True
is_admin = True
max_attempt = 3

def passwordchecker():
    attempt = 0
    try:
        while attempt < max_attempt:
            password = input("Enter password:- ").lower().strip()
            if password.lower() == "q":
                print("Exiting program..")
                break

            if password == "":
                print ("Password cannot be empty! Try again")
                attempt += 1
                continue
            else:
                if is_valid:
                    print("\nValidating password..")
                    if password not in allowed_password:
                        print("Invalid password! Try again")
                        attempt += 1
                        remaining = max_attempt - attempt
                        if remaining > 0:
                            print(f"Attempts remaining: {remaining}")
                        continue
                    else:
                        print("\nLogin Successfull")
                        if is_admin:
                            print("Welcome back admin.")
                        break
                
    except KeyboardInterrupt:
        print ("\nExiting program..")
    
    if attempt >= max_attempt:
        print(f"\n Account locked: Multiple failed attempt {max_attempt}")
            

passwordchecker()