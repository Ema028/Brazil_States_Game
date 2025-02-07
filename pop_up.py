import turtle as t
import random

turtles = []

turtle1 = t.Turtle(shape = "turtle")
turtle1.speed("fastest")
turtle1.penup()
turtles.append(turtle1)

turtle2 = t.Turtle(shape = "turtle")
turtle2.speed("fastest")
turtle2.penup()
turtles.append(turtle2)

turtle3 = t.Turtle(shape = "turtle")
turtle3.speed("fastest")
turtle3.penup()
turtles.append(turtle3)

turtle4 = t.Turtle(shape = "turtle")
turtle4.speed("fastest")
turtle4.penup()
turtles.append(turtle4)

turtle5 = t.Turtle(shape = "turtle")
turtle5.speed("fastest")
turtle5.penup()
turtles.append(turtle5)

directions = [0, 90, 180, 270]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def win():
    for turtle in turtles:
        for i in range (20):
            turtle.color(random_color())
            turtle.setheading(random.choice(directions))
            turtle.forward(50)
