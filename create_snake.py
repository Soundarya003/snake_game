from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.new_snake_list = []
        self.create_snake()
        self.head = self.new_snake_list[0]

    def create_snake(self):
        for pos in positions:
            self.add_snake(pos)

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.new_snake_list.append(new_snake)

    def extend(self):
        self.add_snake(self.new_snake_list[-1].position())

    def move(self):
        for i in range(len(self.new_snake_list) - 1, 0, -1):
            new_x = self.new_snake_list[i - 1].xcor()
            new_y = self.new_snake_list[i - 1].ycor()
            self.new_snake_list[i].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
