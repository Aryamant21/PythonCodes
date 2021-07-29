from turtle import Turtle, position

STARTING_POSTION = [(0 , 0) , (-20 , 0) , (-40 , 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :

    def __init__(self):

        self.tim_snake = []
        self.create_snake()


    def create_snake(self) :
        for position in STARTING_POSTION :
            self.add_segment(position)

    def add_segment(self, position) :
            new_segment = Turtle(shape = "square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.tim_snake.append(new_segment)

    def extend(self) :
        self.add_segment(self.tim_snake[-1].position())

        
    def move(self) :
            for seg_num in range(len(self.tim_snake) - 1 , 0 , -1) :
                new_x = self.tim_snake[seg_num - 1].xcor()
                new_y = self.tim_snake[seg_num - 1].ycor()
                self.tim_snake[seg_num].goto(x = new_x , y = new_y)

            self.tim_snake[0].forward(MOVE_DISTANCE)

    def up(self) :
        if self.tim_snake[0].heading() != DOWN :
            self.tim_snake[0].setheading(UP)

    def down(self) :
        if self.tim_snake[0].heading() != UP :
            self.tim_snake[0].setheading(DOWN)

    def left(self) :
        if self.tim_snake[0].heading() != RIGHT :
            self.tim_snake[0].setheading(LEFT)

    def right(self) :
        if self.tim_snake[0].heading() != LEFT :
            self.tim_snake[0].setheading(RIGHT)