import turtle
import time

turtle.color("red")

turtle.goto(50, 0)
turtle.goto(50, 50)
turtle.goto(0, 50)
turtle.goto(0, 0)

turtle.penup()
turtle.goto(60, 0)
turtle.pendown()
turtle.goto(110, 0)
turtle.goto(110, 50)
turtle.goto(60, 50)
turtle.goto(60, 0)

turtle.penup()
turtle.goto(0, -10)
turtle.pendown()
turtle.goto(0, -60)
turtle.goto(50, -60)
turtle.goto(50, -10)
turtle.goto(0, -10)

turtle.penup()
turtle.goto(60, -10)
turtle.pendown()
turtle.goto(60, -60)
turtle.goto(110, -60)
turtle.goto(110, -10)
turtle.goto(60, -10)

time.sleep(10)
