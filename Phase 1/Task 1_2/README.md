==========================>Task<=======================

# Task 1.2 — Decision Explosion

    Design logic where:
    One input creates at least 5 possible paths
    Each path produces a different outcome
    Only ONE path leads to success
    Write the paths first. Code later.

# State

    start 
    state: prompting
    state: validating_input 
    state: format_invalid
    state: security_conflict
    state: syntax_error
    state: policy_violation
    state: limit_exceed
    state: priority_order
    state: awaiting_retry
    state: success
    end

# Transitions

    start
    prompting + input_received -> validating_input

    validating_input + is_exceed_limit -> limit_exceed
    limit_exceed + giving_time -> awaiting_retry

    validating_input + is_multiple_error -> priority_order
    priority_order + checking_priority_order -> awaiting_retry

    validating_input + is_format_invalid -> format_invalid
    format_invalid + inserting_prompt -> awaiting_retry

    validating_input + is_security_invalid -> security_conflict
    security_conflict + inserting_prompt -> awaiting_retry

    validating_input + is_syntax_invalid -> syntax_error
    syntax_error + inserting_prompt -> awaiting_retry

    validating_input + is_violating_policy -> policy_violtion
    policy_violtion + inserting_prompt -> awaiting_retry

    awaiting_retry + inserting_prompt -> validating_input
    validating_input + is_valid -> success
    end

# Pseudocode

    start
    prompting
    defining error functions
    violates policy
    conflict security
    syntax error
    format error
    limit exceed
    validate prompt
        if prompting violates policy
            print policy violation
            prompting
        if prompting conflict security
            print security conflict
            prompting
        if prompting is syntax error
            print syntax error
            prompting
        if prompting is format error
            print format error
            prompting
        if prompting is limit exceed
            print input limit exceed
            prompting
        if prompting is valid 
            print success
    end


# Task 1.2.1 — Login 

    Design logic where:
    One input username, age, email
    And Login
    Write the paths first. Code later.

# State

    start
    state: inserting_username
    state: inserting_age
    state: inserting_email
    state: confirmation
    state: validating_inputs
    state: invalid_format_details
    state: awaiting_retry
    state: success
    state: inserting_exit
    end

