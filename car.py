
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE
    
    def move(self):
        self.forward(self.move_speed)
    
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
    

    def is_off_screen(self):
        if self.xcor() < -320:
            return True
        else:
            return        
    
        
