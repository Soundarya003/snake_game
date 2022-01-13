from turtle import Turtle, Screen
import random


# here Turtle is superclass, Food is inheriting turtle class
class Food(Turtle):
    # whenever you initialize a new object init gets called
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # usually circle is 20/20, we need it small so making it 10/10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()

    # makes food at random position once the snake eats it
    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x=x_cor, y=y_cor)
