from turtle import Turtle

class ScoreBoard (Turtle) :

    def __init__(self):
        super().__init__()

        self.level = 0

        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x = -250 , y = 275)
        self.write(f"Level = {self.level}" , align = "center", font = ("Courier" , 14 , "normal"))
    
    def update_level(self) :
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}" , align = "center", font = ("Courier" , 14 , "normal"))
    
    
    def game_over(self) :
        tim = Turtle()
        tim.hideturtle()
        tim.write("Game Over !!" , align = "center", font = ("Courier" , 18 , "normal"))