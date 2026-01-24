# Task 3.1 — English-Only Algorithms

    Pick any system:
        Login
        Payment
        File upload
        Job apply
        ATM

    Write:
        INPUTS:
        STATES:
        DECISIONS:
        FAILURES:
        SUCCESS CONDITIONS:
        EXIT POINTS:

No code allowed until this is complete.

# State of Login

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
                    propt try again (y/n)
                    if input != y
                        break 
                    else
                        continue
    end
    