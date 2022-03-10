import turtle
from turtle import Turtle, Screen
import time
from snake import Snake
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

# Turn off the tracer of the screen so that there is no lag between segments of snake
screen.tracer(0)

segments = []

snake = Snake()

# Listen to keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    # Refresh the screen so that there is no lag between segments of snake
    # As all the segments move we update the screen
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()