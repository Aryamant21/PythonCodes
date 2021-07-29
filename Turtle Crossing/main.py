from scoreboard import ScoreBoard
from turtle import Turtle , Screen
from player import Player
from cars import Car
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 620 , height = 620)
screen.bgcolor("white")
screen.tracer(0)

player  = Player()
   
screen.listen()
screen.onkey(player.move , "space")

game_on = True

car = Car()
level = ScoreBoard()


while game_on :

    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_car()
 
    # Detect Crash With Car: 
    for each_car in car.all_cars :
        if player.distance(each_car) < 25 :
            level.game_over()
            game_on = False
    
    # Detect When level has to be raised:
    if player.ycor() > 280 :
        level.update_level()
        car.update_car_speed()
        player.update_player_speed()
        player.reset_position(    )



screen.exitonclick()