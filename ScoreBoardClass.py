from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))
        self.goto(0, 260)

    def show_end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Arial", 24, "normal"))
