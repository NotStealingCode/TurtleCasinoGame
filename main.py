from turtle import Turtle, Screen
import random

user_money = 1000
isrunning = False
continue_playing = True

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while user_money > 0:
    all_turtles = []
    user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color ("
                                                                 "Red/Blue/Green/Yellow/Orange/Purple): ").lower()
    user_bet = screen.numinput(title="Amount", prompt=f"Enter an amount to bet: (You currently have ${user_money})")

    if user_bet > user_money:
        print("Insufficient funds. Restart the game.")
        continue
    isrunning = True
    new_y_position = -160
    for i in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=new_y_position)
        new_y_position += 60
        all_turtles.append(new_turtle)
    while isrunning:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                isrunning = False
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_choice.lower():
                    print(f"You have won! The {winning_turtle} turtle is the winner.")
                    user_money += 2 * user_bet
                else:
                    print(f"You have lost! The {winning_turtle} turtle is the winner.")
                    user_money -= user_bet
                screen.clearscreen()
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
screen.exitonclick()
