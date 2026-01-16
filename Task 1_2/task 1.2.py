prompt = input("Enter to reach right path: ").lower()

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
    for p in priority:
        if p in failure:
            return p, failure
    
    return "Success", []
 