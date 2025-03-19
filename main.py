from turtle import Turtle, Screen
from car import Car
import time
from turtle_manager import Turtles
import random
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Turtles()
score = Scoreboard()

# create list to manage cars
cars = []

car_speed = 5
#add keybaord controls
screen.listen()
screen.onkey(player.go_up, "Up")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    #create cars
    if random.randint(1, 5) == 1:
        new_car = Car()
        new_car.move_speed = car_speed
        cars.append(new_car)

    #move cars
    for car in cars:
        car.move()

        #detect collision with player
        if car.distance(player) < 20:
            player.game_over()
            game_is_on = False
            break

        #detect successful crossing
        if player.ycor() > 280:
            car_speed += 5
            score.increase_score()
            score.update_scoreboard
            player.rest_position()
            for car in cars:
                car.move_speed = car_speed
            
            
    #detect if car is off screen
    for car in cars:
        if car.is_off_screen():
            cars.remove(car)


    






screen.exitonclick()