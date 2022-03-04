import turtle as t
import random

tim = t.Turtle()


########### Draw Shapes ########
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


# shapes -> triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

# number of sides range from [3,11)
for n in range(3, 11):
    change_color()
    for _ in range(n):
        tim.right(360 / n)
        tim.forward(50)
