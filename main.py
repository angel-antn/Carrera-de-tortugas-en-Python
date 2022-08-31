from turtle import Turtle, Screen
import random
import os

color = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
turtles = []
is_race_on = False
text = ''
user_input = ''

screen = Screen()
screen.setup(width=500, height=400)

goal = Turtle(shape='turtle')
goal.color('gray')
goal.penup()
goal.setheading(40)
goal.goto(x=200, y=170)
goal.setheading(270)
goal.pendown()
goal.goto(x=200, y=-170)
goal.setheading(90)

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-124 + i * 50)
    turtles.append(new_turtle)

is_on = True
while is_on:

    validar = True
    while validar:
        user_input = screen.textinput(title="Turtle's race", prompt=f"{text}Write down a color of the"
                                                                    f" rainbow to place a bet").lower()
        if user_input in color:
            text = ''
            validar = False
        else:
            text = "Not valid answer, select a valid rainbow color (red, orange, yellow, green, blue, purple)\n"

    os.system("cls")

    if not validar:
        is_race_on = True

    while is_race_on:

        for i in turtles:

            i.forward(random.randint(0, 10))
            if i.xcor() > 190:
                is_race_on = False
                if i.pencolor() == user_input:
                    text = f"You won, the winner is the {i.pencolor()} turtle\n"
                else:
                    text = f"You lost, the winner is the {i.pencolor()} turtle\n"

    validar = True
    while validar:
        user_input = screen.textinput(title="Turtle's race", prompt=f"{text}Do you want to play "
                                                                    f"again? (yes, no)").lower()
        if user_input == 'yes' or user_input == 'no':
            validar = False
            text = ''
        else:
            text = "Not valid answer, select yes or no\n"

    if user_input == 'no':
        is_on = False
    else:
        for i in range(6):
            turtles[i].setheading(180)
            turtles[i].goto(x=-230, y=-124 + i * 50)
            turtles[i].setheading(0)

screen.exitonclick()
