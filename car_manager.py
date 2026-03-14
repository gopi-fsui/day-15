import math
COLORS = ["red", "orange", "skyblue", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        for x in range(-300,300,random.choice([30,40])):
            self.add_cars(x)
            
    def add_cars(self,x_value):
        car_count = random.randint(0, int(self.move_distance/5))
        for _ in range(car_count):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2, 1)
            new_car.color(random.choice(COLORS))
            # new_car.goto(x_value, (random.randint(-25,25))*10)
            new_car.goto(x_value, random.randint(-25,25)*10)
            self.cars.append(new_car)
            
    def move_forward(self):
        for car in self.cars:
            car.goto(car.xcor()-self.move_distance,car.ycor())
        if random.random() < .25:
            self.add_cars(320)
         
    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
        
    def turtle_acc(self,player):
        for car in self.cars:
            if abs(car.ycor()- player.ycor()) < 15 and math.ceil(player.distance(car)) < 30:
                return True
            elif math.ceil(player.distance(car)) < 25:
                return True
        return False
        
