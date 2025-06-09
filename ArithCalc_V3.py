#Modules
import os
from decimal import Decimal, getcontext
#Variables, Lists and other
getcontext().prec = 28
history = []
#Functions
def clear_shell():
    os.system('cls' if os.name == 'nt' else 'clear')

def parse_input(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        raise ValueError("Input must be in the form: number operator number (e.g., 5 + 3)")
    return parts[0], parts[1], parts[2]

def calculate(a, operator, b):
    try:
        num_a = Decimal(a)
        num_b = Decimal(b)
    except:
        raise ValueError("Both operands must be numbers.")

    if operator == '+':
        return num_a + num_b
    elif operator == '-':
        return num_a - num_b
    elif operator in ['*', 'x', 'X']:
        return num_a * num_b
    elif operator == '/':
        if num_b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num_a / num_b
    else:
        raise ValueError(f"Unsupported operator: {operator}")

print("Calculator V3.0")
print("Enter operations like: 12.5 * 3")
print("Type 'view' to see history, 'ac' or 'c' to clear the screen, 'exit' to quit.")
while True:
    user_input = input("<--$\> ").strip().lower()
    if user_input in ['exit', 'quit']:
        print("Calculator Exited")
        break
    elif user_input in ['ac', 'c']:
        clear_shell()
        continue
    elif user_input == 'view':
        print("Calculation History:")
        if not history:
            print("No calculations yet.")
        else:
            for h in reversed(history[-10:]):
                print(h)
            continue
    try:
        a, op, b = parse_input(user_input)
        result = calculate(a, op, b)
        formatted = f"{a} {op} {b} = {result}"
        print(formatted)
        history.append(formatted)
    except Exception as e:
        print("Error: ", e)