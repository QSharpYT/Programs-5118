import turtle
Bob = turtle.Turtle()
Bob.speed(10) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
numSides = 5
Angle = 360 / numSides
sideLength = 80
Bob.down()
for y in range(24):
  for z in range(numSides):
    Bob.forward(sideLength)
    Bob.right(Angle)
  Bob.right(15)
