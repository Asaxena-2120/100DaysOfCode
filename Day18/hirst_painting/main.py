# Colorgram package is used to extract colors from a given image

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

'''
Make a spot painting of 10*10 screen with circles of radius 20.
idea: https://www.artsy.net/artist-series/damien-hirst-spots
modules used: https://docs.python.org/3/library/turtle.html#turtle.screensize
              https://pypi.org/project/colorgram.py/
'''
import turtle as t
import random

# Because we are using rgb color mode
t.colormode(255)
screen = t.Screen()
tim = t.Turtle()
y=0
color_list = [(245, 243, 238), (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# hiding turtle cursor
tim.hideturtle()


# x= x coordinate of screen, y = y coordinate of screen, gap = gap b/w two dots
def hirst_painting(x, y, gap, dot_radius):
    for i in range(y):
        tim.penup()
        tim.setx(0.0)
        tim.sety(y)
        for j in range(x):
            # print(tim.position())
            color = random.choice(color_list)
            tim.dot(dot_radius,color)
            tim.penup()
            tim.forward(gap)
            tim.pendown()
        y = y+gap


hirst_painting(10,10,50,10)

screen.exitonclick()



