from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape='square')
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[seg - 1].xcor()
            ycor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def update_snake(self):
        new_segment = Turtle(shape='square')
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)
        # new_segment.goto((self.tail.xcor(), self.tail.ycor()))
        self.move()

