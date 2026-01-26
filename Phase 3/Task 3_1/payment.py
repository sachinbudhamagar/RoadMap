Total_Amount = 100


def payment():

    try:
        amount = int(input("Enter Amount:- "))
        if amount <= Total_Amount:
            remaining = Total_Amount - amount
            print(f"\n{amount} paid successfully")
            print(f"Remaining amount is {remaining}\n")
        else:
            print("Transaction failed! Try Again")
    except KeyboardInterrupt:
        print("Exiting program..")
        return


def check():
    print(Total_Amount)


def main():
    print("\n========> Payment System <========\n")
    print("Press 1: Payment")
    print("Press 2: Check Amount")
    print("Press 3: Quit\n")

    while True:
        try:
            press = int(input("Enter no.:- "))
            if press == 1:
                payment()

            elif press == 2:
                check()
            elif press == 3:
                break
            else:
                print("Invalid input! Try again")
                continue
        except KeyboardInterrupt:
            print("Exiting program..")
            break


if __name__ == "__main__":
    result = main()
    print(result)
