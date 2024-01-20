from turtle import *
import time

from FoodClass import Food
from ScoreBoardClass import Scoreboard
from SnakeClass import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
game_is_on = True

screen.listen()
screen.onkey(snake.turn_north, "w")
screen.onkey(snake.turn_west, "a")
screen.onkey(snake.turn_south, "s")
screen.onkey(snake.turn_east, "d")

food = Food()
score = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.elongate(1)
        food.generate_new_food()
        score.update_score()

    for snake_part in snake.snake[2:len(snake.snake):1]:
        if snake.head.distance(snake_part) < 15:
            game_is_on = False
            break

    if abs(snake.snake[0].xcor()) > 290 or abs(snake.snake[0].ycor()) > 290:
        game_is_on = False
        score.show_end_game()

screen.exitonclick()
