FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()
        self.goto(-280,260)
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def game_over(self):
        self.goto(-90,40)
        self.fillcolor("red")
        self.pencolor("black")
        self.begin_fill()
        for _ in range(2):
            self.fd(180)
            self.right(90)
            self.fd(80)
            self.right(90)
        self.end_fill()
        self.goto(0,-10)
        self.write(f"Game over!!",align="center",font=FONT)

