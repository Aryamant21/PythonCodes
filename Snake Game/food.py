from turtle import Turtle
import random
  
class Food (Turtle):
    
    def __init__(self):

        super().__init__()

        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_food()

    def random_food(self) :
        random_xcor = random.randint(-280 , 280)
        random_ycor = random.randint(-280 , 280)
        self.goto(x = random_xcor , y = random_ycor)