from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200, 250)
        self.hideturtle()
        self.lvl = 1
        self.update_score()

    def game_over(self):
        self. goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.lvl}", align="center", font=FONT)
