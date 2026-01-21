Task 2.1 — Nested Conditions Hell

    Create logic with:
    At least 3 nested if levels
    At least 2 early exits
    No duplicated conditions
    If you get confused, that’s the point.


#STATE

    start
    state: inserting_input
    state: checking_validation
    state: exiting_on_invalid
    state: checking_permission
    state: exiting_on_not_granted
    state: matching_input
    state: unmatched
    state: unmatched_allow_retry
    state: exiting_on_success
    end

#TRANSITIONS

    start
    inserting_input + input_received -> checking_validation
    checking_validation + is_invalid -> exiting_on_invalid
    checking_validation + is_valid -> checking_permission
    checking_permission + is_not_granted -> exiting_on_not_granted
    checking_permission + is_granted -> matching_input
    matching_input + is_unmatched -> unmatched_allow_retry
    matching_input + is_matched -> success
    unmatched_allow_retry + is_retry -> inserting_input
    success + is_ouput -> exiting_program
    end

#Pseudocode

    start
    print Enter input or enter quit to exit program
    password is Thunder
    while True
        input
        if input is quit
            break 
        
        if input is not empty
            if permission is_granted
                if input is matched with password
                    print success
                else 
                    print input failed to match
                    continue
            else 
                print permission is not granted
                continue
        else
            print input cannot be empty
            continue
    end
