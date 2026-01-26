class PaymentSystem:
    def __init__(self, total_amount=100):
        self.balance = total_amount

    def payment(self):
        try:
            amount = int(input("Enter Amount:- "))
            if amount <= 0:
                print("Amount must be positive.")

            if amount <= self.balance:
                self.balance -= amount
                print(f"\n{amount} paid successfully")
                print(f"Remaining amount is {self.balance}\n")
            else:
                print(f"Insufficient funds! (Available{self.balance})")
        except ValueError:
            print("Invalid input! Enter number")

    def check(self):
        print(f"\nCurrent balance: {self.balance}")

    def main(self):
        print("\n========> Payment System <========\n")

        while True:
            print("Press 1: Payment")
            print("Press 2: Check Amount")
            print("Press 3: Quit\n")

            try:
                choice = int(input("Enter no.:- "))
                if choice == 1:
                    self.payment()

                elif choice == 2:
                    self.check()
                elif choice == 3:
                    print("Exiting program..")
                    break
                else:
                    print("Invalid input! Enter 1, 2, or 3")
                    continue
            except KeyboardInterrupt:
                print("Exiting program..")
                break


if __name__ == "__main__":
    result = PaymentSystem()
    result.main()
