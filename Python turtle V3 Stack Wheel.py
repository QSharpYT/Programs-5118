import turtle
Bob = turtle.Turtle()
Bob.speed(10) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
numSides = 6
Angle = 360 / numSides
sideLength = 50
Bob.down()
for y in range(12):
  for z in range(numSides):
    Bob.forward(sideLength)
    Bob.right(Angle)
  Bob.right(30)
numSides = 3
Angle = 360 / numSides
sideLength = 25
Bob.down()
for y in range(24):
  for z in range(numSides):
    Bob.forward(sideLength)
    Bob.right(Angle)
  Bob.right(15)
numSides = 10
Angle = 360 / numSides
sideLength = 50
Bob.down()
for y in range(12):
  for z in range(numSides):
    Bob.forward(sideLength)
    Bob.right(Angle)
  Bob.right(30)
Bob.right(5)
numSides = 36
Angle = 360 / numSides
sideLength = 15
Bob.down()
for y in range(12):
  for z in range(numSides):
    Bob.forward(sideLength)
    Bob.right(Angle)
  Bob.right(30)
