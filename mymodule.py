def greet(name):
    # return f"Hello,{name}!"
    print(f"Hello,{name}!")


def age(age):
    return int(age)

def add (a,b):
    result = a + b
    return f"The addition of both numbers is {result}"

def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        return a / b
    else:
        return "Invalid operation. Choose 'add', 'sub', 'mul', or 'div'."
