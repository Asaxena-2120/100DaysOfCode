import turtle as t
import random

screen = t.Screen()
# Setting up 500px wide and 400px height screen
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
                                                         "red, orange, yellow, green, blue, purple ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

# Make six turtles
for i in range(6):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])
    all_turtles.append(tim)
    x, y =tim.position()
    print(x,y)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:

            is_race_on = False
            turtle.write(f"{turtle.color()[0].upper()} WON ", True, align="center")
            if turtle.color()[0] == user_bet:
                print("You guessed right! ")
            else:
                print(f"{turtle.color()[0].upper()} won. You lose! ")
            continue
        turtle_pos= random.randint(1,10)
        turtle.forward(turtle_pos)


screen.exitonclick()