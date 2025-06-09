#Variables
nums = None
User_Input = None
calc1 =  None
calc2 =  None
calc3 =  None
ccalc = None
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
print("Calculator V2.0 \n Please put a space between the numbers and the operotor(+ - * /): ")
while User_Input != 'exit':
    print("Type 'exit' to stop the calculator")
    print("Type 'view' to view previous calculations in the session")
    User_Input = input("<--$\>")
    calc3 = calc2
    calc2 = calc1
    calc1 = ccalc
    try:
        if User_Input == 'view':
            print(calc1)
            print(calc2)
            print(calc3)
        else:
            ccalc = User_Input + ' = ' + str(calculate(*find_nums(User_Input)))
            print(ccalc)
    except Exception as e:
        print("Error: ", e)
    

print("Calculator Exited")