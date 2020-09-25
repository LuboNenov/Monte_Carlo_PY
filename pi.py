import turtle
import random

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.tracer(1e100)
myPen.speed(1e100)
window = turtle.Screen()
window.bgcolor("#FFFFFF")

def drawSquare(x,y,width):
  myPen.penup()
  myPen.goto(x,y)
  myPen.pensize(3)
  myPen.color("#333333")
  myPen.pendown()
  for side in range(0,4):
    myPen.forward(width)
    myPen.right(90)
  myPen.pensize(1)

def drawCircle(x,y,radius):
  myPen.penup()
  myPen.goto(x,y-radius)
  myPen.pensize(2)
  myPen.color("#333333")
  myPen.pendown()
  myPen.circle(radius)
  myPen.pensize(1)


def drawDot(x,y,color):
  myPen.penup()
  myPen.goto(x,y-1)
  myPen.pendown()
  myPen.fillcolor(color)
  myPen.color(color)
  myPen.begin_fill()
  myPen.circle(1)
  myPen.end_fill()

radius= 180
color = "#000000"
total = 2500
totalIn = 0

drawSquare(-radius,radius,2*radius)
drawCircle(0,0,radius)

for dots in range(total):
  x = random.randint(-radius,radius)
  y = random.randint(-radius,radius)

  distance = (x**2 + y**2)**0.5
  if distance<radius:
    color = "#FF0000"
    totalIn += 1
  else:
    color = "#0000FF"
  drawDot(x,y,color)
myPen.getscreen().update()
pi = 4*(float(totalIn)/total)
print("Pi :" + str(pi))