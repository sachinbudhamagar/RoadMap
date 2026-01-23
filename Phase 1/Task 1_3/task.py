def function1():
    return None

def function2():
    return "We got something"

def function3():
    condition1 = function1()
    condition2 = function2()
    if condition1 == None:
        return f"{condition1}"
    else:
        return f"{condition2}"


def main():
    step1 = function1()
    print(f"{step1}")

    step2 = function2()
    print(f"{step2}")
    
    step3 = function3()
    print(f"{step3}")

main()
