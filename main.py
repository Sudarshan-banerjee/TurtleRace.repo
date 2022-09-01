from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Who's gonna win the race? pick a colour: ")
colours = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
all_turtles = []
y = -120
for color in colours:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y = y+40
    all_turtles.append(new_turtle)

if user_bet:
    game_on = True
else:
    game_on = False

while game_on:
    turtle_distance = randint(0, 10)

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_colour = turtle.pencolor()
            if user_bet == winning_colour:
                print(f"you won the game! {winning_colour} won the game.")
            else:
                print(f"you lost! {winning_colour} won the race.")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
