from turtle import Screen
from create_snake import Snake
from food import Food
from scoreboard import Score
import time

# setting up the screen
screen = Screen()
# setting the width and height
screen.setup(width=600, height=600)
# setting up the bg color
screen.bgcolor("Black")
# setting up the title for the game
screen.title("Snake Game")
# turn turtle animation off so we can create objects
screen.tracer(0)

# creating objects of classes imported
snake = Snake()
food = Food()
score = Score()

# using in-built screen functions to make it work according to pressing the buttons
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# initializing a variable which is True when it's not colliding
is_not_collide = True

while is_not_collide:
    # to refresh the screen
    screen.update()
    # so we can slow down and delay the refresh
    time.sleep(0.1)
    snake.move()
    # detect collision with wall
    if snake.head.xcor() > 297 or snake.head.ycor() > 297 or snake.head.xcor() < -297 or snake.head.ycor() < -297:
        print("You've lost")
        score.finish()
        is_not_collide = False
    # detect collision with tail
    # using the concept of slicing we're excluding the head and then finding if it'll collide with other parts
    for i in snake.new_snake_list[1:len(snake.new_snake_list)]:
        if snake.head.distance(i) < 10:
            is_not_collide = False
            score.finish()

    # to detect snake colliding with food
    # trying to get distance between two turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.calculate_score()

screen.exitonclick()
