import turtle as t

tim = t.Turtle()
screen = t.Screen()


def go_forward():
    tim.forward(10)


def go_backward():
    tim.backward(10)


def clockwise():
    tim.left(10)


def counter_clockwise():
    tim.right(10)


def clear():
    screen.resetscreen()


screen.onkey(fun=go_forward, key="Up")
screen.onkey(fun=go_backward, key="Down")
screen.onkey(fun=counter_clockwise, key="Left")
screen.onkey(fun=clockwise, key="Right")
screen.onkey(fun=clear, key="c")

# Listens to keyboard events or key-events
screen.listen()
screen.exitonclick()