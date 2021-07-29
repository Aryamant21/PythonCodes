from turtle import Turtle
import random

COLORS = ["red" , "orange", "yellow" , "green", "blue" , "purple"]
CAR_MOVE_DIST = 8
CAR_MOVE_INCREMENT = 2

class Car :
    
    def __init__(self):
        self.all_cars  = []
        self.car_move_distance = 8

    def create_cars(self) :
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid = 1 , stretch_len = 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_ycor = random.randint(-245 , 250)
            new_car.goto( x = 300 , y = random_ycor)
            self.all_cars.append(new_car)
    
    def move_car(self) :
        for car in self.all_cars :
            car.backward(self.car_move_distance)
        
    def update_car_speed(self) :
        self.car_move_distance += CAR_MOVE_INCREMENT
