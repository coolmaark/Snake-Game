from turtle import Turtle
start = [(0, 0), (-20, 0), (-40, 0)]
moved = 20
u, d, l, r = 90, 270, 180, 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in start:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(moved)

    def up(self):
        if self.head.heading() != d:
            self.head.setheading(u)

    def down(self):
        if self.head.heading() != u:
            self.head.setheading(d)

    def left(self):
        if self.head.heading() != r:
            self.head.setheading(l)

    def right(self):
        if self.head.heading() != l:
            self.head.setheading(r)
