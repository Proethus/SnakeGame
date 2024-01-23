from turtle import *

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = list[Turtle]()
        self.elongate(3)
        self.head = self.snake[0]
        self.has_turned = False
        self.next_turn = None

    def elongate(self, number_of_pieces_to_add):
        for index in range(0, number_of_pieces_to_add):
            new_snake = Turtle("square")
            new_snake.hideturtle()
            new_snake.pensize(20)
            new_snake.penup()
            new_snake.color("white")
            self.snake.append(new_snake)
            if len(self.snake) > 1:
                new_snake.goto(self.snake[-1].xcor() - 20, self.snake[-1].ycor())
            else:
                new_snake.goto(0, 0)
            new_snake.showturtle()

    def reset_snake(self):
        for segment in self.snake[3: len(self.snake): 1]:
            self.snake.remove(segment)
            segment.hideturtle()
            del segment
        self.head.goto(0, 0)

    def move(self):
        prev_pos_x = self.head.xcor()
        prev_pos_y = self.head.ycor()
        self.head.forward(MOVE_DISTANCE)
        self.has_turned = False
        if self.next_turn is not None:
            #     current_direction = self.head.heading()
            #     if not abs(current_direction - self.next_turn) == 180:
            self.head.setheading(self.next_turn)
            self.next_turn = None
        for piece in range(1, len(self.snake)):
            next_prev_pos_x = self.snake[piece].xcor()
            next_prev_pos_y = self.snake[piece].ycor()
            self.snake[piece].goto(prev_pos_x, prev_pos_y)
            prev_pos_x = next_prev_pos_x
            prev_pos_y = next_prev_pos_y

    def turn_north(self):
        if not self.head.heading() == 270 and not self.has_turned:
            self.head.setheading(90)
            self.has_turned = True
        elif not self.head.heading() == 270:
            self.next_turn = 90

    def turn_west(self):
        if not self.head.heading() == 0 and not self.has_turned:
            self.head.setheading(180)
            self.has_turned = True
        elif not self.head.heading() == 0:
            self.next_turn = 180

    def turn_east(self):
        if not self.head.heading() == 180 and not self.has_turned:
            self.head.setheading(0)
            self.has_turned = True
        elif not self.head.heading() == 180:
            self.next_turn = 0

    def turn_south(self):
        if not self.head.heading() == 90 and not self.has_turned:
            self.head.setheading(270)
            self.has_turned = True
        elif not self.head.heading() == 90:
            self.next_turn = 270
