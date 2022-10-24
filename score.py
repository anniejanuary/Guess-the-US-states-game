from turtle import Turtle

ALIGNMENT = 'center'
FONT2 = ('BankGothic Md BT', 17, 'bold')

class Score:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 1

    # winning message
    def game_over(self):
        self.win_message = Turtle()
        self.win_message.hideturtle()
        self.win_message.pu()
        self.win_message.color("red")
        self.win_message.goto(0, 250)
        self.win_message.write("Congrats, you fabulous beast!", font=FONT2, align=ALIGNMENT)


