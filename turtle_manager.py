from turtle import Turtle

class Turtles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.speed(0)
        self.move_speed = 10
    
    def go_up(self):
        self.forward(self.move_speed)
    
    def go_down(self):
        self.backward(self.move_speed)
    
    def rest_position(self):
        self.goto(0, -280)
    
    def level_up(self):
        self.move_speed += 3
        self.rest_position()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Poppins", 24, "normal"))
