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

    idle + enter_personal_details_progress -> waiting_for_personal_details
    waiting_for_personal_details + personal_details_submitted -> validating_personal_details

    validating_personal_details + valid -> personal_details_validated
    validating_personal_details + invalid -> personal_details_validation_failed

    personal_details_validated + upload_cv_progress -> waiting_for_cv
    waiting_for_cv + cv_chosen -> cv_selected

    cv_selected + validation_started -> validating_cv
    validating_cv + valid -> cv_validated
    validating_cv + invalid -> cv_validation_failed

    cv_validated -> application_ready
    application_ready + requested_submit -> submission_in_progress

    submission_in_progress + succeed -> application_submitted
    submission_in_progress + failed -> submission_failed
    
    personal_details_validation_failed + retry_requested -> application_ready
    cv_validation_failed + retry_requested -> waiting_for_cv
    submission_failed + retry_requested -> awaiting_retry
    submission_failed + cancel_requested -> cancelled

    application_submitted -> exiting_program

# Pseudocode

    STATE = "idle"

    WHILE system is running:

        IF STATE = "idle"
            DISPLAY "1. Start Application 2. Exit"
            wait for user_input

            IF user_chooses_start:
                STATE = "waiting_for_personal_details(name, age, degree, experience)"
            ELSE IF user_chooses_exit:
                STATE = "exiting_program"

        ELSE IF STATE == "waiting_for_personal_details":
            DISPLAY "Enter your personal details:"
            COLLECT name, email, phone, address

            IF validation_passed:
                STORE personal_details
                STATE = "personal_details_validated"
            ELSE:
                STORE error_message
                STATE = "personal_details_validation_failed"

        ELSE IF STATE == personal_details_validation_failed:
            DISPLAY ask user either to exit or retry
            INPUT cancel or retry

            IF user enter cancel:
                STATE = "cancelled"
            ELSE IF user enter retry:
                STATE = "waiting_for_personal_details"
        
        ELSE IF STATE == "personal_details_validated":
            DISPLAY "personal details saved successfully"
            STATE = "waiting_for_cv"

        ELSE IF STATE == "waiting_for_cv"
            DISPLAY upload your CV(pdf/DOCX, 5MB)
            wait for file_selection

            IF file_selected:
                STATE = "cv_selected"
                STORE selected file
            ELSE IF user cancel:
                STATE = "cancelled"
        
        ELSE IF STATE == "cv_selected":
            DISPLAY validating cv(type, size)
            IF validation_passed:
                STATE = "cv_validated"
            ELSE:
                STATE = "cv_validation_failed"
                STORE error message

        ELSE IF STATE == "cv_validation_failed":
            DISPLAY "CV Error: " + error_message
            DISPLAY "either to retry or cancel"

            IF user_chooses_retry:
                STATE = "waiting_for_cv"
            ELSE:
                STATE = "cancelled"

        ELSE IF STATE == "cv_validated"
            DISPLAY "CV uploaded and validated"
            STATE = "application_ready"

        ELSE IF STATE == "application_ready":
            DISPLAY "Review your application"
            DISPLAY personal_details
            DISPLAY cv_filename
            DISPLAY "1. Submit Application 2. Edit Details 3. Cancel"
            INPUT 1/2/3:
            
            wait for user action
            IF user enter submit:
                STATE = "submission_failed"
            ELSE IF user edit:
                STATE = "waiting_for_personal_details"
            ELSE:
                STATE = "cancelled"

        ELSE IF STATE == "submission_failed":
            IF progress submitted:
                STATE = "application_submitted"
            ELSE:
                STORE error message
                STATE = "awaiting_retry"

        ELSE IF STATE == awaiting_retry:
            ask user either to retry or cancel
            DISPLAY "1. Retry 2. Cancel"

            IF user enter retry:
                STATE = "application_ready"
            ELSE IF user cancels:
                STATE = "cancelled"

        ELSE IF STATE == "application_submitted"
            DISPLAY "Application submitted successfully!"
            SEND confirmation_email
            STATE = "idle"

        ELSE IF STATE == "cancelled":
            DISPLAY "Application cancelled"
            CLEAR selected_file
            RESET form
            STATE = "idle"

        ELSE IF STATE == "exiting_program":
            DISPLAY "Thank you for using Job Application System"
            BREAK  loop
        
        
# English only Algorithm of Job Apply system

    1. DEFINE STATE as idle
    2. INITIATE WHILE LOOP
    3. WHILE STATE is idle, provide option for start application and exit, and wait for user input
            IF user chooses start, STATE is waiting_for_personal_dtails else exiting_program
    4. ELSE IF STATE is waiting_for_personal_details, enter personal details, and validate it
            IF validation_passed store personal details and STATE is personal_details_validated 
            ELSE STORE error_message and STATE IS personal_details_validation_failed
    5. ELSE IF STATE is personal_details_validation_failed DISPLAY and ASK user either to retry or cancel
            IF user enter cancel STATE is cancelled ELSE STATE is waiting_for_personal_details
    6. ELSE IF STATE is personal_details_validated, DISPLAY personal details saved and STATE is waiting_for_cv
    7. ELSE IF STATE is waiting_for_cv, DISPLAY upload your cv and wait for file_selection
            IF file_selected, STATE is cv_selected and store selected file 
            ELSE IF user cancel STATE is cancelled
    8. ELSE IF STATE is cv_selected, DISPLAY validating cv 
            IF validation_passed STATE is cv_validated ELSE STATE is cv_validation_failed, STORE error message
    9. ELSE IF STATE is cv_validation_falied, DISPLAY cv error with error_message and ask user either to retry or cancel
            IF user_chooses_retry STATE is waiting_for_cv ELSE STATE is cancelled
    10. ELSE IF STATE is cv_validated, DISPLAY cv uploaded, and validated and STATE is application_ready
    11. ELSE IF STATE is application_ready, DISPLAY review application, personal_details, cv_filename, and ask user for Submit, Edit, or Cancel
            IF user enter submit STATE is submission_failed 
            ELSE IF user edit STATE is waiting_for_personal_details 
            ELSE STATE is cancelled
    12. ELSE IF STATE is submission_failed STATE is application_submitted ELSE STATE is awaiting_retry and STORE error message
    13. ELSE IF STATE is awaiting_retry, ask user either to retry or cancel
            IF user enter retry STATE is application_retry
            ELSE IF user cancels STATE is cancelled
    14. ELSE IF STATE is application_submitted STATE is idle, DISPLAY application submitted successfully and send confirmation email
    15. ELSE IF STATE is cancelled STATE is idle, DISPLAY appliation cancelled and reset form
    16. ELSE IF STATE is exiting_program, BREAK loop and DISPLAY Thank you for using Job Application System message

# 5. State of ATM

    state:
