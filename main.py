import turtle
import time
import random

delay = 0.1

window = turtle.Screen()
window.title("Snake")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

bodySegments = []

