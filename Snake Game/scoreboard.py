from turtle import Turtle

class Score(Turtle) :
    def __init__(self) :
        super().__init__()
        self.score = 0
        
        self.goto(x = 0, y = 270)
        self.color("white")
        self.scoreboard()
        self.hideturtle()
        self.penup()

    def scoreboard(self) :
        self.write(arg = f"Score = {self.score}" , align = "center" , font=("Courier" , 20 , "normal"))

    def increase_score(self) :
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self) :
        self.clear()
        self.goto(x = 0 , y = 0)
        self.write(arg = f"Score = {self.score}\nGAME OVER !!" , align = "center" , font=("Courier" , 20 , "normal"))

        
        
        