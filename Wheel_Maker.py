import turtle

ident = input("10 digit number NO SPACES, COMMAS OR DASHES: ")
try:
    v1 = int(ident[0:2])
    v2 = int(ident[2:4])
    v3 = int(ident[4:6])
    v4 = int(ident[6:8])
    v5 = int(ident[8:10])
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.ht()
    for i in range(v1):
        t.forward(v2)
        t.right(v3)
        t.backward(v2)
        t.right(v3)
        t.backward(v4)
        t.right(v5)
except:
    print("10 digit number only, rerun the program")

#Try 5065372618
#Try 3609653987
#Try 3562843727