
import math

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        for x in range(-280,280,random.choice([40,50,60])):
            self.add_cars(x)


    def add_cars(self,x_value):
        car_count = random.randint(0, 2)
        for _ in range(car_count):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2.5, 1)
            new_car.color(random.choice(COLORS))
            # new_car.goto(x_value, (random.randint(-25,25))*10)
            new_car.goto(x_value, random.randint(-250,250))
            self.cars.append(new_car)

    def move_forward(self):
        for car in self.cars:
            car.goto(car.xcor()-self.move_distance,car.ycor())

        if random.random() < .2:
            self.add_cars(280)


    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT


    def turtle_acc(self,player):
        for car in self.cars:
            if abs(car.ycor()- player.ycor()) < 20 and math.ceil(player.distance(car)) < 30:
                print(f"first one {car.ycor()} - {player.ycor()} = {abs(car.ycor()- player.ycor())} and dis is {math.ceil(player.distance(car))}")
                return True
            elif math.ceil(player.distance(car)) < 20:
                print(f"Second - {math.ceil(player.distance(car))}")
                return True

        return False
