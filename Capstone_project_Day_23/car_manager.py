from turtle import Turtle
import random

Color = ("red","blue","green","yellow")
class CarManager(Turtle):

    def __init__(self):
        self.move = 10
        self.increment = 5
        self.all_car = []

    def create_car(self):
        radom_chance = random.randint(1,6)
        if radom_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(Color))
            new_car.setheading(180)
            new_car.shapesize(1,2)
            new_car.setposition(300,random.randint(-250,250))
            self.all_car.append(new_car)

    def motion(self):
        for car in self.all_car:
            car.forward(self.move)

    def level_up(self):
        self.move += self.increment
