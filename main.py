from turtle import Turtle, Screen

tim= Turtle()
screen= Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.forward(-10)
def turn_left():
    tim.right(30)
def turn_right():
    tim.left(30)
def clear_drawing():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)


screen.mainloop()