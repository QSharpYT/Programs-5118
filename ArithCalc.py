#Variables
nums = None
User_Input = None
#Functions
def find_nums(UIn):
    try:
        nums = UIn.split()
        return nums
    except Exception as e:
        print("Error:", e)
        return None

def calculate(numa, op, numb):
    num_a = int(numa)
    num_b = int(numb)
    if op == '+':
        return num_a + num_b
    elif op == '-':
        return num_a - num_b
    elif op == '*' or op == 'x':
        return num_a * num_b
    elif op == '/':
        return num_a / num_b
    else:
        return 'unknown operator, please use +-*/'
#Main Code
print("Calculator V1.0 \n Please put a space between the numbers and the operotor(+ - * /): ")
while User_Input != 'exit':
    User_Input = input("<--$\>")
    print("Type 'exit' to stop the calculator")
    try:
        print(User_Input, ' = ', str(calculate(*find_nums(User_Input))))
    except Exception as e:
        print("Error: ", e)

print("Calculator Exited")