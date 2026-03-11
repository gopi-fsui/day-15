import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_forward()
    if player.ycor() > player.finish_line:
        player.reset_pos()
        scoreboard.increase_level()
        cars.increase_speed()
        # cars.mo

    if cars.turtle_acc(player):
        game_is_on = False
        scoreboard.game_over()


screen.mainloop()
