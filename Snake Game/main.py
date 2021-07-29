from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("AT21's Snake Game")
screen.tracer(0)

user_level = screen.textinput(title="Set Your Difficulty !" , prompt= "Select your Difficulty (Easy/Hard)")

snake = Snake()

food = Food()

score = Score() 

screen.listen()

screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

screen.update()

game_on = True

while game_on :
    screen.update()
    
    if user_level.lower() == "hard" :
        time.sleep(0.1)
    else :
        time.sleep(0.15)

    snake.move()
      
    
    # Detect collition with food
    if snake.tim_snake[0].distance(food) < 14 :
        food.random_food()
        score.increase_score()
        snake.extend()

    # detect collition with Wall :
    if snake.tim_snake[0].xcor() > 288 or snake.tim_snake[0].xcor() < -288 or  snake.tim_snake[0].ycor() > 288 or snake.tim_snake[0].ycor() <-288 :
        game_on = False
        score.game_over()

    # Collition with itself:
    for segment in snake.tim_snake[1 : ] :

        if snake.tim_snake[0].distance(segment) < 12 :
            game_on = False
            score.game_over()



screen.exitonclick()

