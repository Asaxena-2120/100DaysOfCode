import turtle as t
import random
'''
modules used: turtle, random
idea: https://en.wikipedia.org/wiki/Spirograph 
'''
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

###########  Spirograph ########
size_of_gap= 5
for _ in range(int(360/size_of_gap)):
  tim.color(random_color())
  tim.speed("fastest")
  tim.circle(100)
  tim.setheading(size_of_gap)
  size_of_gap = size_of_gap + 5

screen = t.Screen()
screen.exitonclick()



