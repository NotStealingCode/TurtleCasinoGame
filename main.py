from turtle import Screen
import turtle as t
import random

john = t.Turtle()
john.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

size_of_gap = 0

for create_shape in range(0, 72):
    john.color(random_color())
    john.circle(100)
    john.setheading(size_of_gap)
    size_of_gap += 5

screen = Screen()
screen.exitonclick()
