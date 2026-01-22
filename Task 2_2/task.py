print("\nEnter ok for beast mode")
print("Enter q to quit/exit")

def bestMode():
    try:
        while True:
            mode = input("\nTurn on the mode:- ")
            if mode == "q":
                print("Exiting program..")
                break

            if mode == "ok":
                print("Beast mode activated")
                break
            else:
                print("Invalid input!")
                continue
    except KeyboardInterrupt:
        print("Exiting program..")

bestMode()