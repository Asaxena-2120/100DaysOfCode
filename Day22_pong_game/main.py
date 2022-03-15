from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Turn off the animation
screen.tracer(0)

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Ball


screen_length = screen.window_width()
screen_height = screen.window_height()

game_is_on = True
while game_is_on:
    # to slow down the ball
    time.sleep(ball.move_speed)
    # Turn on the animation when paddles have reach their initial positions
    screen.update()
    ball.move()

    # if ball hits the top or bottom, ball should bounce
    if ball.ycor() > (screen_height//2)-2 or ball.ycor() < -(screen_height//2)-2 :
        ball.bounce_y()

    # Detect collision with r_paddle or right paddle
    # check the contact
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or \
            (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()


    # If ball hits right wall and misses right paddle
    if ball.xcor() > (screen_length//2):
        ball.reset_position()
        scoreboard.l_point()

    # If ball hits left wall and misses left paddle
    if ball.xcor() < -(screen_length//2):
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()