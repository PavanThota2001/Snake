starting_positions = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class snake:
    def __init__(self):
        self.segments = []
        self.start()
        self.move()
        self.up()
        self.down()
        self.left()
        self.right()

    def start(self):
        for position in starting_positions:
            self.add_segment(position)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading != LEFT:
            self.segments[0].setheading(RIGHT)
    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    def extend(self):
        self.add_segment(self.segments[2].position())



