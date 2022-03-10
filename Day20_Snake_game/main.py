import turtle
from turtle import Turtle, Screen
'''
Typical Snake Game
'''

screen = Screen()

# Setup screen size
screen.setup(height=600, width=600)

# Setting up background color of screen
screen.bgcolor("black")

# Setting up title of the screen
screen.title("Snake Game")

# CREATE A SNAKE BODY, Create 3 turtles and position them like each
# turtle should be a white square (default: size 20*20)
for i in range(0,3):
    tim = Turtle()
    tim.color("white")
    tim.shape("square")
    tim.goto(x=i*-20, y =0)



screen.exitonclick()