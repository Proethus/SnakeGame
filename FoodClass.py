from turtle import *
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.generate_new_food()

    def generate_new_food(self):
        self.shape("circle")
        self.color("blue")
        self.fillcolor("blue")
        self.pensize(20)
        self.penup()
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.speed("fastest")
        self.goto(rand_x - rand_x % 20, rand_y - rand_y % 20)
