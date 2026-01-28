# Task 1.3 — Return Discipline

    Create 3 functions where:
    One returns a value
    One returns nothing
    One returns conditionally
    Explain (to yourself):
    Where execution goes after each return


# State

    start
    state: calling_fuction
    state: executing_function
    state: after_function_call
    state: function_terminates
    state: exiting_program
    end

# Transitions

    start
    calling_fuction + function_received -> executing_function
    executing_function + returning_none -> after_function_call

    executing_function + returning_value -> after_function_call
    executing_function + returning_value_conditionally -> after_function_call
    
    after_function_call + program_decides_exit -> function_terminates
    function_terminates + program_end -> exiting_program
    end


# Pseudocode

    start
    define function1
        return none
    define function2
        return value
    define function3
        result1 is equal function1
        result2 is equal function2
        if result1 is empty
            return result1
        else
            return result2
    
    def mainfunction
        step1 is equal to function1
        print step1
    
        step2 is equal to function2
        print step2
    
        step3 is equal to function3
        print step3
    
    calling mainfunction
    execution continue
