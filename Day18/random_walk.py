import turtle as t
import random

'''
idea: https://en.wikipedia.org/wiki/Random_walk
module used: turtle
'''

tim = t.Turtle()

########### Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


# move_list = [tim.left(90),tim.right(90)]
# tim.pensize(5)
# while True:
#   tim.color(random.choice(colours))
#   move = random.randint(1,4)
#   if move == 1:
#     tim.right(90)
#   elif move == 2:
#     tim.left(90)
#   elif move == 3:
#     tim.forward(10)
#   else:
#     tim.backward(10)
#   tim.forward(10)
tim.pensize(15)
tim.speed("fastest")
directions = [0, 90, 180, 270]
for _ in range(200):
    # tim.color(random.choice(colours))
    change_color()
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()



