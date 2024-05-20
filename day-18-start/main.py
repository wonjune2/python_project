import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)




for _ in range(72):
    tim.color(random_color())
    tim.circle(120)
    tim.left(5)



screen = t.Screen()
screen.exitonclick()