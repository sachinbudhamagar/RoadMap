while True:
    try:    #Unexpected Error handler
        inserting_input = int(input("\nEnter 1 for prompt and 2 for exit:- "))
        if inserting_input == 1:
            prompt = input("\nEnter name:- ").lower() #Converts input into lowercase
            #validating_input
            if prompt.strip() == "":   #Logic for empty and whitespace error
                print("Prompt cannot be empty or contain whitespace") #invalid_format_input
            else:
                print(f"{prompt} accepted auccessfully") #success
            continue #awaiting_retry
        elif inserting_input == 2: #inserting_exit
            print("\nExiting program...")
            break 
        else:
            print("Invalid input! Enter 1 or 2:")
    except KeyboardInterrupt:
        print(f"Exiting program...")
        break
    