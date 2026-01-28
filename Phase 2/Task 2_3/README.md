# Task 2.3 — Silent Failure

    Design a function that:
    Fails silently in one case
    Raises error in another
    Continues normally otherwise
    Do NOT print errors unless required.

# State

    start
    state: inserting_input
    state: silent_fail_condition
    state: check_raise_error
    state: add_to_list
    state: final_output
    state: exit
    end

# Transition

    start
    inserting_input + input_received -> silent_fail_condition

    silent_fail_condition + is_valid -> check_raise_error
    silent_fail_condition + is_invalid -> add_to_list

    check_raise_error + is_error -> terminate
    add_to_list + input_added -> final_output
    
    final_output + is_exit -> terminate
    end

# Pseudocode

    start

    creatinng empty list
    
    inserting input
    if input triggers error
        raise error
    else
        pass
    
    if input is valid
        add input in list
        print list
        return
