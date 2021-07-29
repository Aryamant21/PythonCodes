from turtle import Turtle,Screen, color
import random

race = False 

screen = Screen()

screen.setup(width = 500 , height = 400)

screen.bgcolor("seagreen")

user_bet = screen.textinput(title="Make Your Bet !" , prompt= "Which Turtle do you think will win? Enter a Colour")

colors  = ["red", "orange" , "yellow", "green", "blue", "purple"]

y_pos = [-100 , - 60 , -20 , 20 , 60 , 100]

all_turtles = []

for x in range (0,6) :
    new_tim = Turtle(shape="turtle")
    new_tim.color(colors[x])
    new_tim.penup()
    new_tim.goto(x = -225, y = y_pos[x])
    all_turtles.append(new_tim)
 
if user_bet :
    race = True

while race :
    for turtle in all_turtles :
        if turtle.xcor() > 240 :

            race = False

            winning_color = turtle.pencolor()

            if winning_color == user_bet :
                print(f"You win!!! The {winning_color} turtle wins the race\n")
            else :
                print(f"You lose :(  The {winning_color} turtle wins the race\n")

        random_distance = random.randint(0 , 6)
        turtle.forward(random_distance)


