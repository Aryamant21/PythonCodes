from turtle import Turtle

STARTING_POS = (0 , -280)
MOVE_INCREMENT = 2

class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.move_distance = 10
        
        self.shape("turtle")
        self.color("black")
        self.shapesize(1.2)
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)
    
    def move(self): 
        self.forward(self.move_distance)
    
    def update_player_speed(self):
        self.move_distance += MOVE_INCREMENT
    
    def reset_position(self):
        self.goto(STARTING_POS)