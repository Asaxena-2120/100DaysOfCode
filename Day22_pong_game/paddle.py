from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,x,y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x=self.x, y=self.y)

    def up(self):
        # get the current y coordinate
        y_cord = self.ycor()
        self.goto(x=self.xcor(), y=y_cord + 20)

    def down(self):
        y_cord = self.ycor()
        self.goto(x=self.xcor(), y=y_cord - 20)






