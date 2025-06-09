#Modules
import math
#Main Code, Variables, and Output
mode = input("Which side are you calculating? (a, b, or c): ").lower()
if mode == 'c':
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = math.sqrt(a ** 2 + b ** 2)
elif mode == 'b':
    a = float(input("Enter side a: "))
    c = float(input("Enter side c: "))
    if c <= a:
        print("Invalid: Hypotenuse must be longer than side a.")
        exit()
    b = math.sqrt(c ** 2 - a ** 2)
elif mode == 'a':
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    if c <= b:
        print("Invalid: Hypotenuse must be longer than side b.")
        exit()
    a = math.sqrt(c ** 2 - b ** 2)
else:
    print("Invalid mode. Please choose a, b, or c.")
    exit()
print(f"Side a: {round(a, 2) if 'a' in locals() else 'calculated'}")
print(f"Side b: {round(b, 2) if 'b' in locals() else 'calculated'}")
print(f"Side c: {round(c, 2) if 'c' in locals() else 'calculated'}")