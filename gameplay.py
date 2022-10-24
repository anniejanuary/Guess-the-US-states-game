from turtle import Turtle
import pandas

ALIGNMENT = 'left'
FONT1 = ('Calibri', 9)

class GamePlay:
    def __init__(self):
        self.state_names_turtle = Turtle()
        self.state_names_turtle.hideturtle()
        self.state_names_turtle.pu()
        # creates states_pool
        self.states_pool = []
        data = pandas.read_csv("50_states.csv")
        for state in data.state:
            self.states_pool.append(state)

    def write_state_name(self, state_name, x, y):
        self.state_names_turtle.goto(x, y)
        self.state_names_turtle.write(f"{state_name}", font=FONT1, align=ALIGNMENT)

    def write_missing_states(self, state_name, x, y):
        self.state_names_turtle.color("red")
        self.state_names_turtle.goto(x, y)
        self.state_names_turtle.write(f"{state_name}", font=FONT1, align=ALIGNMENT)
