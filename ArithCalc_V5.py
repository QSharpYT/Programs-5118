# Modules
import os
import math
from decimal import Decimal, getcontext
import re

# Precision setting
getcontext().prec = 28
history = []

# Functions
def clear_shell():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            if os.getenv("TERM"):
                os.system('clear')
            else:
                print("\n" * 100)  # fallback: print blank lines
    except:
        print("\n" * 100)

def safe_eval(expr):
    # Replace constants and functions
    expr = expr.replace('pi', 'math.pi')
    expr = expr.replace('e', 'math.e')
    expr = expr.replace('^', '**')  # allow ^ as power operator
    expr = re.sub(r'√\(([^)]+)\)', r'math.sqrt(\1)', expr)  # √(x) to math.sqrt(x)
    expr = expr.replace('sqrt', 'math.sqrt')  # also allow sqrt()

    # Basic input check — allow numbers, math functions/constants
    if not re.fullmatch(r"[0-9\.\+\-\*/\^\(\) xX, math.sqrtpie]+", expr):
        raise ValueError("Invalid characters in expression.")

    expr = expr.replace('x', '*').replace('X', '*')

    # Replace standalone numbers with Decimal (but not math constants/functions)
    expr = re.sub(r'(?<![a-zA-Z_])(\d+\.\d+|\d+)', r'Decimal("\1")', expr)

    return eval(expr, {"Decimal": Decimal, "math": math})

# Main Program
print("Calculator V5.0")
print("Supports: +, -, *, /, ^ (exponents), pi, e, sqrt(x), √(x), and full expressions")
print("Type 'view' to see history, 'ac' or 'c' to clear the screen, 'exit' to quit.")

while True:
    user_input = input("<--$> ").strip()
    if user_input.lower() in ['exit', 'quit']:
        print("Calculator Exited")
        break
    elif user_input.lower() in ['ac', 'c']:
        clear_shell()
        continue
    elif user_input.lower() == 'view':
        clear_shell()
        print("Calculation History:")
        if not history:
            print("No calculations yet.")
        else:
            for h in reversed(history[-10:]):
                print(h)
        continue
    try:
        result = safe_eval(user_input)
        formatted = f"{user_input} = {result}"
        print(formatted)
        history.append(formatted)
    except Exception as e:
        print("Error:", e)
