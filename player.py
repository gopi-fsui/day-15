STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.finish_line = FINISH_LINE_Y
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.goto(STARTING_POSITION[0],self.ycor()+MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
