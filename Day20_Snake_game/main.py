import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
'''
Typical Snake Game: stores highest score each time player plays game
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
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15: # because food is 10*10
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # Detect collision with tail
    # if head collides with any segment in the tail -> trigger game over
    for segment in snake.segments[1:]: # skip head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()