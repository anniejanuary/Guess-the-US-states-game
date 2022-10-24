import turtle
from turtle import Screen
import pandas
from tkinter import messagebox

from gameplay import GamePlay
from score import Score

screen = Screen()
screen.title("50 US States Quiz")
screen.addshape("blank_states_img.gif") # adding the shape of blank_states_img.gif to the screen
turtle.shape("blank_states_img.gif") # displays the image as screen background
gameplay = GamePlay()
score = Score()

data = pandas.read_csv("50_states.csv")

while len(gameplay.states_pool) > 0:
    user_answer = (screen.textinput(title=f"{score.score}/50 States", prompt="Enter a US state name / or 'done' when you're out of ideas:")).title()

    for row in data.state:
        #exiting and saving not guessed states to csv:
        if user_answer == "Done":
            # df = pandas.DataFrame(gameplay.states_pool)
            # df.to_csv("states_to_learn.csv")
            # break
            for state in gameplay.states_pool:
                gameplay.write_missing_states(state_name=state, x=int(data[data.state == state].x),
                                      y=int(data[data.state == state].y))
        # if user enters a correct state...
        if user_answer == row:
            #... that they haven't guessed before
            if user_answer in gameplay.states_pool:
                gameplay.states_pool.remove(user_answer)
                score.increase_score()
                gameplay.write_state_name(state_name=row, x=int(data[data.state == user_answer].x),
                                          y=int(data[data.state == user_answer].y))
            # The alert when user tries guessing a previously guessed state
            else:
                messagebox.showinfo("Hi there, hello", "You've already guessed this state. Try another.")
# once user guesses all 50 states:
else:
    score.game_over()

turtle.mainloop() # doesnt close the Output screen even if I click on it which screen.exitonclick() would





# Getting states coordinates in blank_states_img.gif
# def get_mouseclick_coordinates(mouseclickx, mouseclicky):
#     # why these "mouseclickx, mouseclicky" are needed:
#     # https://stackoverflow.com/questions/48869611/turtle-onscreenclick-not-behaving-as-expected
#     print(mouseclickx, mouseclicky)
#
# screen.listen()
# screen.onscreenclick(get_mouseclick_coordinates)
