max_attempts = 10

def violates_policy(prompt):
    banned = ["spam", "hack", "illegal"]
    return any(word in prompt for word in banned)

def conflict_security(prompt):
    risk = ["admin", "root", "password"]
    return any(word in prompt for word in risk)

def syntax_error(prompt): 
    return prompt.count("(") != prompt.count(")")

def format_error(prompt):
    return len(prompt) < 3 or len(prompt) > 500

def validating_prompt(prompt: str, attempt_num: int):
    failure = []

    if attempt_num > max_attempts:#check if attempts exceeded
        failure.append("Prompt limit exceed")

    if violates_policy(prompt):
        failure.append("Policy violation")

    if conflict_security(prompt):
        failure.append("Security conflict")

    if syntax_error(prompt):
        failure.append("Syntax error")

    if format_error(prompt):
        failure.append("Format error")
    
    priority = [
        "Prompt limit exceed", 
        "Policy violation", 
        "Security conflict", 
        "Syntax error", 
        "Format error"
        ]
    
    for p in priority: #checks error priority order list 
        if p in failure: 
            return p, failure #Exit on 1st priority error
    
    return "success", [] #print success if no error is found

def main():
    attempt_count = 0

    print(f"\nEnter prompt to validate (max {max_attempts} attempts")
    print(f"Type q for quit or exit\n")

    while True:
        prompt = input("Enter prompt to validate: ").lower().strip()

        if prompt == "q":
            print("Exiting program ...")
            break

        attempt_count += 1

        result, error = validating_prompt(prompt, attempt_count)
        print(f"\nValidation Result: {result}")

        if error: #Print error reason
            print(f"\nError found: {error}")
        
        if result == "success":
            print("Validation passed")
            break

        if attempt_count >= max_attempts:
            print(f"\nMaximum attempts ({max_attempts}) reached. Exiting")
            break

        remaining = max_attempts - attempt_count
        print (f"Attempts Remaining: {remaining}\n")

if __name__ == "__main__":
    main()