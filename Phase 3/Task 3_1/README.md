# Task 3.1 — English-Only Algorithms

    Systems:
        1. Login
        2. Payment
        3. File upload
        4. Job apply
        5. ATM


# 1. State of Login system

    start
    state: inserting_credentials
    state: validating_credentials
    state: invalid_credentials
    state: awaiting_retry
    state: reach_max_attempts
    state: success
    state: exiting_program
    end

# Transitions

    start
    inserting_credentials + credentials_received -> validating_credentials

    validating_credentials + is_valid -> success
    validating_credentials + is_invalid -> invalid_credentials

    invalid_credentials + attempts_remaining -> awaiting_retry
    invalid_credentials + max_attempts_reached -> reach_max_attempts

    awaiting_retry + user_decide_continue -> inserting_credentials
    awaiting_retry + user_decide_exit -> exiting_program

    reach_max_attempts + force_exit -> exiting_program
    end
    
# Pseudocode

    start
    attempts is 0
    max_attempts is 3
    while True
        input credentials
        if input is exit
            break
        if valid
            print success
            return 
        else
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if attempts >= max_attempts
                break
            else
                print invalid_credentials
                awaiting_retry
                    prompt try again (y/n)
                    if input != y
                        break 
                    else
                        continue
    end
    

# English only Algorithm of Login system

    1. define attempts and max attempts
    2. input username and password or quit program
    3. if input is exit, terminate program 
    4. if username and password is valid, print login successful
    5. if username and password is invalid
    6. count attempts and subtract it from max attempts
    7. if attempts reached max attempts, terminate program
    8. if attempts is remaining ask user either wants retry or not
    9. if press y, restarting input else terminate program


# 2. State of Payment System

    start
    state: inserting_input
    state: validate_input
    state: invalid_input
    state: check_funds
    state: insufficient_funds
    state: awaiting retry
    state: success
    state: exiting_program
    end

# Transitions

    start
    inserting_input + input_received -> validate_input
    inserting_inupt + exit_requested -> exiting_program

    validate_input + is_invalid -> invalid_input
    validate_input + is_valid -> check_funds

    check_funds + is_insufficient -> insufficient_funds
    check_funds + is_sufficient -> success

    invalid_input + is_retry -> awaiting_retry
    insufficient_funds + is_retry -> awaiting_retry

    awaiting_retry -> inserting_input
    awaiting_retry + exit_requested -> exiting_program 
    
    success -> exiting_program
    end

# Pseudocode

    start
    create class

        initital function 
            total_fund is 100

        define payment function
            while True
                inserting_input

                if inserting_input is exit
                    exit program

                if inserting_input is integer/number
                    if inserting_input is less or equal total_fund
                        subtract input from total_fund
                        print successfully payed with remaining balance
                    else
                        print insufficient funds
                        waiting retry
                
                else
                    print invalid input
                    awaiting_retry
                    continue
            
        define checkFunds function
            print total funds

        main function
            while True
                choose program to run
                if input is 1
                    call payment function
                if input is 2
                    call checkFunds function
                if input is 3 
                    exit program
                    break

    create object 
    result is class
    call main function
    end


# English only Algorithm of Payment system

    create class and initial function for total fund as shared class state
    crete a payment function that accepts user input
    if user input is exit command, terminate program
    validate the input to ensure it as a number
    if input is invalid display input message and allow retry
    if input is valid, check whether the amount is les than or equals to available funds
    if the amount exceeds the available funds, display insufficient funds and allow retry
    if sufficient funds are available, subtract the amount and confirm successfull payment
    create seperate function to dispaly funds when user requested
    create main function allow to choose between making payment, checking funds, or exiting
    create object for class and invoke the main function start the program

# 2. State of File Upload system

    state: inserting_file
    state: validating_file
    state: file_not_selected
    state: upload_click
    state: invalid_file
    state: awaiting_retry
    state: upload_failure
    state: uploaded_successfully
    state: exit_program

# Transitions
    
    inserting_file + file_received -> validating_file
    inserting_file + is_empty -> file_not_selected

    validating_file + is_valid -> upload_click
    validating_file + is_invalid -> invalid_file

    file_not_selected + is_retry -> awaiting_retry
    file_not_selected + is_exit -> exit_program

    invalid_file + is_retry -> awaiting_retry
    invalid_file + is_exit -> exit_program

    awaiting_retry + is_continue -> inserting_file
    awaiting_retry + is_exit -> exit_program

    upload_click + is_fail -> upload_failure
    upload_click + is_success -> uploaded_successfully
    upload_click + is_cancel -> exit_program

    uploaded_successfully -> exit_program