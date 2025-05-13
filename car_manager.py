from turtle import Turtle
from random import randint,choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.generate_car()
    
    def generate_car(self):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1.0, stretch_len=2.0)
            car.penup()
            car.color(choice(COLORS))
            x_pos = randint(270,280)
            y_pos = randint(-260, 260)
            car.goto(x_pos, y_pos)
            self.cars.append(car)

    def move_car(self):
            for car in self.cars:
                car.backward(self.move_distance)

    def next_level(self):
          self.move_distance += 10
        
        
