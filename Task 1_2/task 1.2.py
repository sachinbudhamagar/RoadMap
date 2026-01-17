prompt = input("Enter to reach right path: ").lower()

def violates_policy():
    banned = ["spam", "hack", "illegal"]
    return any(word in prompt for word in banned)

def conflict_security():
    risk = ["admin", "root", "password"]
    return any(word in prompt for word in risk)

def syntax_error(): 
    return prompt.count("(") != prompt.count(")")

def format_error():
    return len(prompt) < 3 or len(prompt) > 10

def validating_prompt(prompt: str):
    failure = []
    if violates_policy(prompt):
        failure.append("Policy violation")
    if conflict_security(prompt):
        failure.append("Security conflict")
    if syntax_error(prompt):
        failure.append("Syntax error")
    if format_error(prompt):
        failure.append("Format error")
    
    priority = ["Policy violation", "Security conflict", "Syntax error", "Format error"]
    for p in priority: #checks error priority order list 
        if p in failure: 
            return p, failure #Exit on 1st priority error
    
    return "Success", [] #print success if no error is found
 
result, error = validating_prompt(prompt) #calling validation function 
print(f"Validation Result: {result}")

if error: #Print error reason
    print(f"Error found: {error}")