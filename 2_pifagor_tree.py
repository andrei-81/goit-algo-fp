import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    angle = 45

    position = t.position()
    heading = t.heading()

    t.left(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    t.setposition(position)
    t.setheading(heading)

    t.right(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    t.setposition(position)
    t.setheading(heading)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  

    level = int(input("введіть рівень рекурсії: "))
    length = 100

    t.up()
    t.goto(0, -screen.window_height() / 2 + 20)
    t.down()

    draw_pythagoras_tree(t, length, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
