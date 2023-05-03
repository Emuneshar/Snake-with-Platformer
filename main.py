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