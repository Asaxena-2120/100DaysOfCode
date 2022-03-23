'''
Inspired from: https://www.sporcle.com/games/g/states
Guess the name of states on the map
'''
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Add image file to screen to give shape to turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# We already stored all the coordinates in 50_states.csv for this project, but below is the method how it is done
# def get_mouse_click_coor(x, y):
#     # Get the coordinates of each state
#     # For this we will get coordinates of the point where we click on the screen/map
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# # Keep screen open even though we click on the screen
# turtle.mainloop()

# read 50_states csv
states = pandas.read_csv('50_states.csv')
state_name_list = states.state.to_list()

answer_list =[]
game_is_on = True
while game_is_on:
    # get the input from user
    # convert user input to Title format
    answer_state = screen.textinput(title=f"{len(answer_list)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == 'Exit':
        # save missed states into a csv
        new_data = pandas.DataFrame(state_name_list)
        new_data.to_csv("states_to_learn.csv")

        game_is_on = False


    # get row from 50_states.csv that matches user's guess
    if states[states['state']==answer_state].empty:
        continue
    else:
        state_details = states[states['state']==answer_state]
        answer_list.append(answer_state)
        state_name_list.remove(answer_state)

        # make a turtle object to move cursor to write data
        tim= turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state_details['x']),int(state_details['y']))

        # item() get the first value of the series
        tim.write(state_details.state.item())

    # If player guessed all the names of the states
    if len(answer_list)==50:
        game_is_on= False



