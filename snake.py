from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.timmies = []
        self.create_snake()
        self.head = self.timmies[0]

    def create_snake(self):
        for turt in POSITION:
            self.add_timmy(turt)

    def add_timmy(self, position):
        timmy = Turtle("square")
        timmy.penup()
        timmy.color("White")
        timmy.goto(position)
        self.timmies.append(timmy)

    def extend_snake(self):
        self.add_timmy(self.timmies[-1].position())

    def move(self):
        for turt_num in range(len(self.timmies) - 1, 0, -1):
            new_x = self.timmies[turt_num - 1].xcor()
            new_y = self.timmies[turt_num - 1].ycor()
            self.timmies[turt_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
