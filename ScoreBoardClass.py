from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.penup()
        file = open("high_score.txt", "r")
        self.high_score = int(file.readline())
        self.write(f"Score: {self.score} | High score: {self.high_score}", False, "center", ("Arial", 24, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_high_score()
        self.write(f"Score: {self.score} | High score: {self.high_score}", False, "center", ("Arial", 24, "normal"))
        self.goto(0, 260)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("high_score.txt", "w")
            file.write(f"{self.high_score}")

    def reset_score(self):
        self.score = -1
        self.update_score()
