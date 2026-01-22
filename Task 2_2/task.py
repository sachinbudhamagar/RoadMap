print("\nEnter ok for beast mode")
print("Enter q to quit/exit")
beast_mode = True

def bestMode():
    try:
        while beast_mode:
            mode = input("\nTurn on the mode:- ")
            if mode.lower() == "q":
                print("Exiting program..")
                break

            if mode.lower() == "ok":
                print("Beast mode activated")
                user_decision = input("\nDo you wish to continue? y/n:- ").lower()
                if user_decision != "y":
                    print("Exiting program.. ")
                    break
                else:
                    continue
            else:
                print("Invalid input!")
                continue
    except KeyboardInterrupt:
        print("Exiting program..")

bestMode()