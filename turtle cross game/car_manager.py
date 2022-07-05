from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_Y=random.randint(0,280)
CARS=[]

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
   
    def create_car(self):
        random_chance=random.randint(1,6)
        if  random_chance==1:
            car=Turtle()   
            car.penup()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.resizemode("user")
            car.turtlesize(1,2) 
            ran_y=random.randint(-250,250)
            car.goto(280,ran_y)
            self.all_cars.append(car)

    def level_up(self): 
        self.car_speed += MOVE_INCREMENT  
    
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
