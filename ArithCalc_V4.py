# Modules
import os
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
    if not re.fullmatch(r"[0-9\.\+\-\*/\(\) xX ]+", expr):
        raise ValueError("Invalid characters in expression.")
    expr = expr.replace('x', '*').replace('X', '*')
    tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/()]', expr)
    converted_expr = ""
    for token in tokens:
        if re.fullmatch(r'\d+\.\d+|\d+', token):  # If it's a number
            converted_expr += f"Decimal('{token}')"
        else:
            converted_expr += token
    return eval(converted_expr, {"Decimal": Decimal})
# Main Program
print("Calculator V4.0")
print("Full expressions like: 12 + 373 * 373 + 32 , are now supported")
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
