import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.onkey(key="Up", fun=player.move)
    screen.onkey(key="Down", fun=player.move_down)
    car.move_car()
    counter +=1
    if counter == 6:
        car.generate_car()
        counter = 0
    for single_car in car.cars:
        if player.distance(single_car) < 20:
            score.gameover()
            game_is_on = False
   
    if player.ycor() > 270:
        player.goto(0,-280)
        car.next_level()
        score.level_up()
    screen.update()    
screen.exitonclick()