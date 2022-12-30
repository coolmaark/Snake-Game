from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("red")
        self.speed("fastest")
        self.newloc()

    def newloc(self):
        nx = random.randint(-280, 280)
        ny = random.randint(-280, 280)
        self.goto(nx, ny)
