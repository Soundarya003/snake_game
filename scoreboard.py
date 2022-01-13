from turtle import Turtle

Align = "LEFT"
Font = ('Arial', 15, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(x=-70, y=270)
        self.hideturtle()
        self.update()

    def update(self):
        # using the write function to display text on screen and update it
        self.write(arg=f"Score: {self.count} ", move=False, align=Align, font=Font)

    # if the snake collides with wall or tail then
    def finish(self):
        self.goto(x=-80, y=0)
        self.write(arg=f"GAME OVER!!", move=False, align=Align, font=Font)

    # everytime the snake eats food it'll increment the score
    def calculate_score(self):
        self.count += 1
        self.clear()
        self.update()
