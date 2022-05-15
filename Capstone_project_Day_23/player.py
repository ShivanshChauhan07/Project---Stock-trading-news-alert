from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.setheading(90)
        self.penup()
        self.positions = (0,-280)
        self.setpos(self.positions)
        self.move=10

    def go_up(self):
        new_y = self.ycor() + self.move
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - self.move
        self.goto(self.xcor(),new_y)

    def resets(self):
        self.setpos(self.positions)

    def collision(self):
        pass
