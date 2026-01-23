# Task 2.2 — Loop Ownership

    Create a loop where:
    Loop condition does NOT control exit
    Exit happens from inside logic
    Loop must exit in at least 2 different ways


# State

    state: loop_active
    state: inserting_input
    state: check_format
    state: awaiting_retry
    state: success
    state: user_decide_exit
    state: exiting_program


# Transition

    start
    loop_active + loop_activated -> inserting_input
    inserting_input + input_received -> check_format
    check_format + is_invalid -> awaiting_retry
    awaiting_retry + user_decide_yes -> inserting_input
    awaiting_retry + user_decide_no -> exiting_program
    inserting_input + is_valid -> success
    success + user_decide_yes -> inserting_input
    success + user_decide_no -> exiting_program 
    end

# Pseudocode

    list is a test
    beast mode is True
    
    define  function
        try:
            while beast mode
                input Turn on beast mode 
                if input is exit
                    break

                if input is test
                    print success 
                    user decide with yes or no
                    if yes
                        continue
                    else
                        break
                else
                    print invalid input
                    continue
        except keyboard Interrupt  
            print exiting program
                
