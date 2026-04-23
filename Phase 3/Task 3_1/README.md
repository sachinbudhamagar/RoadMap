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

# 3. State of File Upload system

    state: idle
    state: waiting_for_file
    state: file_selected
    state: file_validation_failed
    state: file_validated
    state: ready_to_upload
    state: upload_in_progress
    state: upload_fail
    state: upload_completed
    state: calcalled
    state: exiting

# Transitions
    
    idle + start_upload_process -> waiting_for_file
    waiting_for_file + file_chosen -> file_selected

    file_selected + validate_file -> validating
    validating + valid -> file_validated
    validating + invalid -> file_validation_failed

    file_validated -> ready_to_upload
    file_validation_failed + retry_request -> awaiting_retry

    awaiting_retry + continue -> waiting_for_file
    awaiting_retry + is_exit -> exiting_program

    ready_to_upload + upload_request -> upload_in_progress

    upload_in_progress + failed -> upload_failed
    upload_in_progress + completed -> upload_completed
    upload_in_progress + cancelled -> exiting_program

    upload_completed -> exiting_program

# Pseudocode
    
    start
    STATE = "idle"
    WHILE system_running:

        IF state == "idle":
            Display "Ready. Select a file to upload"
            WAIT FOR user_action

            IF user_select_file:
                STATE = "file_selected" 
                STORE selected file
            
            ELSE IF user_exits:
                STATE = "exiting_program"

        ELSE IF STATE == "file_selected":
            VALIDATE file (size, type, name)

            IF validation_passed:
                STATE = "file_validated"
            ELSE:
                STATE = "file_validation_failed"
                STORE error_message
            
        ELSE IF STATE == "file_validated":
            DISPLAY "Ready_to_upload file. Press upload to continue"
            WAIT FOR user_action

            IF user_clicks_upload:
                STATE = "upload_in_progress"
            ELSE IF user_cancels:
                STATE = "cancelled"
            ELSE IF user_changes_file:
                STATE = "waiting_for_file"

        ELSE IF STATE == "upload_in_progress":
            START uploading file
            SHOW progress bar

            IF upload_successfull:
                STATE = "upload_completed"
            ELSE:
                STATE = "upload_failed"
                STORE error_message

        ELSE IF STATE == "upload_completed":
            DISPLAY "Upload Successfull!"
            RESET form
            STATE = "idle"
        
        ELSE IF STATE == "upload_failed":
            DISPLAY error_message
            ASK user: "Retry or Cancel?"

            IF user_clicks_retry:
                STATE = "ready_to_upload"
            ELSE:
                STATE = "Cancelled"

        ELSE IF STATE == "cancelled":
            CLEAR selected_file
            RESET form
            STATE = "idle"
        
        ELSE IF STATE == "exiting"
            BREAK loop
            
# English only Algorithm of File Upload System

    1: Define STATE as "idle"
    2: Initiate WHILE loop
    3: IF STATE is "idle", display "ready for file upload" and wait for user action
        IF user select file, store file and 
        IF user select exit, exit program
    4: ELSE IF STATE is "file_selected", validate file(name, size, type)
        IF validation passed STATE is "file_validated", 
        ELSE STATE is "file_validation_failed" and display "error message"
    5: ELSE IF STATE is "file_validated", dispaly "Ready to upload file" and wait for user action
        IF user click upload STATE IS "upload_in_process", 
        ELSE IF user cancels STATE is "canelled", 
        ELSE IF user changes file STATE is "waiting_for_file"
    6: ELSE IF STATE is "upload_in_progress", start uploading and show progress bar
        IF upload successfull STATE is "upload_completed" ELSE "upload_failed", and store error message
    7: ELSE IF STATE is "upload_completed" display "upload successfull" and reset form where STATE is "idle"
    8: ELSE IF STATE is "upload_failed" display "error_message" and ask user either to "retry or cancel"
        IF user click retry restart program where STATE is "ready_to_upload" else STATE is "cancelled"
    9: ELSE IF STATE is "cancelled"  clear selected file, reset form and restart where STATE is "idle"
    10: ELSE IF STATE is "exiting" exit program and break loop

# 4. State of Job Apply

    state: idle
    state: waiting_for_personal_details
    state: personal_details_validated
    state: personal_details_validation_failed
    state: waiting_for_cv
    state: cv_selected
    state: cv_validated
    state: cv_validation_failed
    state: application_ready
    state: submission_failed
    state: application_submitted
    state: awaiting_retry
    state: cancelled
    state: exiting_program

# Transitions

    idle + enter_personal_details_process -> waiting_for_personal_details
    waiting_for_personal_details + personal_details_submitted -> validating_personal_details

    validating_personal_details + valid -> personal_details_validated
    validating_personal_details + invalid -> personal_details_validation_failed

    personal_details_validated + upload_cv_process -> waiting_for_cv
    waiting_for_cv + cv_chosen -> cv_selected

    cv_selected + cv_uploaded -> validating_cv
    validating_cv + valid -> cv_validated
    validating_cv + invalid -> cv_validation_failed

    cv_validated -> application_ready
    application_ready + requested_submit -> submission_in_process
    
    submission_in_process + succeed -> application_submitted
    submission_in_process + failed -> submission_failed
    
    submission_failed + retry_requested -> awaiting_retry
    submission_failed + cancel_requested -> cancelled

    application_submitted -> exiting_program

# 5. State of ATM

    state:
