# Task 2.2 — Loop Ownership

    Create a loop where:
    Loop condition does NOT control exit
    Exit happens from inside logic
    Loop must exit in at least 2 different ways


# STATE

    state: loop_active
    state: inserting_input
    state: check_format
    state: awaiting_retry
    state: success
    state: user_decide_exit
    state: exiting_program


# TRANSITIONS

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