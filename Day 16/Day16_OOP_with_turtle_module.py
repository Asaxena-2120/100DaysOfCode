#!usr/bin/env python3
'''
Learning OOP concepts with https://docs.python.org/3/library/turtle.html turtle module

'''
# import modules
import turtle

# From module turtle using Turtle class to make an object timmy
timmy = turtle.Turtle()

# From module turtle using Screen class to make an object the_screen
the_screen = turtle.Screen()

# Using functions from Turtle class

# polygon shapes allowed: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
timmy.shape('turtle')
timmy.color('yellow')
print(timmy.position())
timmy.forward(100)
print(timmy.position())

the_screen.bgcolor("black")

the_screen.exitonclick()