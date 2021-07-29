from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("AT21's Pong Game")
screen.bgcolor("red")

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))

game_on = True

screen.listen()

screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")

screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")

ball = Ball()

score = Scoreboard()

while game_on :
    time.sleep(ball.move_speed)
    ball.move()

    #Detect when Ball touches above and boottom boundaries
    if ball.ycor() < -275 or ball.ycor() > 275 :
        ball.bounce_y()
    
    #Detect when Ball goes out of Bounds
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < - 335 :
        ball.bounce_x()
    
    #Destect when right player misses
    if ball.xcor() > 400 : 
        ball.reset_position()
        score.l_point()

    #Detect when left player misses
    if ball.xcor() < -400 :
        ball.reset_position()
        score.r_point()


screen.exitonclick()