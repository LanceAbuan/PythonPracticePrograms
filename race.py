import turtle as trt
import random as rd
import math
import time

"""
    Hello, this is code that was written in order to make a randomized turtle race using the turtle library.
    This code allows the user to customize different parameters of the race.
    Firstly, the user can choose between 2-8 different competitors in the race.
    Secondly, the user can choose the name for each of the turtles. Each of the names is unique.
    Thirdly, the user can choose the color for each racer. Each of the colors is unique.
"""

# TODO get rid of this comment

# Serves no functional purpose other than improves quality of life

# The function "confirmation" is used for the Y/N questions
def confirmation(S):
    # The return statement in this function returns 2 booleans
    # The first boolean is if the input is a valid answer for a Y/N question
    # The second boolean returns True if S is "yes" and False if S is "no".

    # This if statement checks if "S", the input string, is a "yes" or "no"
    if S.lower() == "y" or S.lower() == "n":
        if S.lower() == "y":
            answer = True
        else:
            answer = False
        return True, answer

    # If "S", the input string, is not a "yes" or "no", then return Null
    else:
        return False, None

# This function uses bubble sorting to sort the list of tuples
# Bubble sorting generally runs faster than most sorting algorithms if the list length is small
# The tuple that comes in here has the following formatting:


def sort_tuple(list_of_tuples):

    for i in range(len(list_of_tuples)):
        for j in range(len(list_of_tuples) - 1 - i):
            if list_of_tuples[j][0][0] < list_of_tuples[j + 1][0][0]:
                placeholder = list_of_tuples[j + 1]
                list_of_tuples[j + 1] = list_of_tuples[j]
                list_of_tuples[j] = placeholder

    return list_of_tuples



def make_board():

    print("Drawing the board now...")
    wn = trt.Screen()
    wn.tracer(0)
    rootwindow = wn.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    drawer = trt.Turtle()
    drawer.shape("blank")
    drawer.penup()
    drawer.setposition(-350, 350)
    drawer.speed(0)

    for iter in range(21):
        drawer.pendown()
        drawer.forward(25)
        drawer.write(iter)
        drawer.right(90)
        for j in range(10):
            drawer.forward(30)
            drawer.penup()
            drawer.forward(30)
            drawer.pendown()
        drawer.penup()
        drawer.left(180)
        drawer.forward(600)
        drawer.right(90)
    drawer.penup()

    for iterate in range(len(contestant_list)):
        turtle_list[iterate].penup()
        turtle_list[iterate].setpos(-350, 300 - iterate * 70)
    race_incomplete = True
    for element in turtle_list:
        element.penup()


    countdown_label = trt.Turtle()
    countdown_label.penup()
    countdown_label.shape("blank")
    countdown_label.setposition(300,200)
    countdown_label.pendown()
    countdown_label.write("Start in: ",align="center",font = ("Arial",30,"normal"))

    countdown = trt.Turtle()
    countdown.shape("blank")
    countdown.penup()
    countdown.setposition(300,150)
    countdown.pendown()

    for i in range(3, 0, -1):
        for j in range(45, 0, -1):
            countdown.write(i,font=("Arial",j,"normal"))
            wn.update()
            time.sleep((3/135))
            countdown.clear()
    countdown_label.clear()
    countdown.write("Go!", align="center",font = ("Arial",30,"normal"))
    wn.update()


    start_time = time.time()
    while race_incomplete:

        for i in range(0,len(turtle_list)):
            run(turtle_list[i], turtle_list, i)

        wn.update()

        list_of_winners = []

        for i in range(0,len(turtle_list)):
            if turtle_list[i].xcor() > 175:
                race_incomplete = False
                list_of_winners.append((contestant_list[i], turtle_list[i].pencolor()))

        if not race_incomplete:
            racer_placings = []
            for i in range(len(turtle_list)):
                racer_placings.append((turtle_list[i].pos(), contestant_list[i]))

        time.sleep(.01)

    congrats = trt.Turtle()
    congrats.shape("blank")
    congrats.penup()
    congrats.speed(10)
    racer_placings = sort_tuple(racer_placings)

    for i in range(len(racer_placings)):
        congrats.setpos(racer_placings[i][0][0], racer_placings[i][0][1] + 20)
        congrats.write(str(i + 1) + ". " + racer_placings[i][1])

    if len(list_of_winners) == 1:
        print("The winner of this race is:")
        for a, b in list_of_winners:
            print(a, "-", b)

    elif len(list_of_winners) > 1:
        print("The winners of this race are: ")
        for a, b in list_of_winners:
            print(a, "-", b)

    drawer.setpos(0,-300)
    countdown.clear()
    drawer.write("The race lasted for %.3s seconds!" % (time.time() - start_time), move=False, align="center", font=("Arial", 20, "normal"))


def choose_color(color_list, list_of_contestants, list_of_turtles, individual, number):
    if not individual:
        iteration = 0
        while iteration < len(list_of_contestants):
            print("Choose a color(number) for Contestant", list_of_contestants[iteration])

            for j in range(len(color_list)):
                print(str(j + 1) + ".", color_list[j])
            color_choice = input()

            if integer_check(color_choice):
                color_choice = int(color_choice)
                if (color_choice > 0) and (color_choice <= len(color_list)):
                    list_of_turtles[iteration].color(color_list[color_choice - 1])
                    del color_list[color_choice - 1]
                    iteration += 1
                else:
                    print("Please input a valid number.")
            else:
                print("Please input a valid number.")
        return color_list, list_of_contestants, list_of_turtles
    else:
        print("Choose a color(number) for Contestant", list_of_contestants[number])
        for j in range(len(color_list)):
            print(str(j + 1) + ".", color_list[j])
        ind_color_choice = input()
        if integer_check(ind_color_choice):
            color_choice = int(ind_color_choice)
            if (color_choice > 0) and (color_choice <= len(color_list)):
                color_list.append(list_of_turtles[number].pencolor())
                list_of_turtles[number].color(color_list[color_choice - 1])
                del color_list[color_choice - 1]
            else:
                print("Please input a valid number.")
        else:
            print("Please input a valid number.")
        return color_list, list_of_contestants, list_of_turtles


def integer_check(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def collision(turtle, steps, list_of_turtles, number):
    safe_path = True
    future_xcor = steps * math.cos(turtle.heading())
    future_ycor = steps * math.sin(turtle.heading())
    collider_list = list_of_turtles.copy()

    del collider_list[number]
    for collider in collider_list:
        obj_xcor = collider.xcor()
        obj_ycor = collider.ycor()
        if (abs(future_xcor - obj_xcor) < 20 and abs(future_ycor - obj_ycor) < 20):
            safe_path = False
        elif (future_ycor > 340 or future_ycor < -240):
            safe_path = False

    return safe_path


def run(turtle, list_of_turtles, iteration):
    init_angle = turtle.heading()
    proper_angle = False
    collision_count = 0
    while not proper_angle:
        turtle.setheading(init_angle)
        steps = rd.randint(1, 2)
        if collision_count < 20:
            if 10 < turtle.heading() < 30:
                turtle.right(rd.randint(0, 3))
            elif 350 > turtle.heading() > 330:
                turtle.left(rd.randint(0, 3))
            else:
                turtle.right(rd.randint(-3, 3))
            proper_angle = collision(turtle, steps, list_of_turtles, iteration)
            collision_count += 1
        else:
            steps = 0
            proper_angle = True
    #turtle.setpos(turtle.xcor()+steps*math.cos(math.radians(turtle.heading())), turtle.ycor()+steps*math.sin(math.radians(turtle.heading())))
    turtle.forward(steps)


# This creates the turtles
creating = True
while creating:
    valid_count = False
    while not valid_count:
        print(
            "Hello! Welcome to the turtle race! How many turtles would you like to make?\nMin Amount: 2\nMax Amount: 8")
        turtle_count = input()
        if not integer_check(turtle_count):
            print("Please enter a valid integer.")
        elif int(turtle_count) < 2 or int(turtle_count) > 8:
            print("Please enter an integer between 2 and 8")
        else:
            confirmed = False
            turtle_count = int(turtle_count)
            while not confirmed:
                print("You said you want to make", turtle_count, "turtles. Is this true? Y/N")
                valid, count_bool = confirmation(input())
                if valid:
                    valid_count = count_bool
                    print("Moving onto the next phase...")
                    confirmed = True
                else:
                    print("Please enter a valid input.")

    picking_names = True
    while picking_names:
        contestant_list = []
        print("Please name each turtle.")

        i=0
        while i < turtle_count:
            print("The name of racer number", i + 1, "is: ")
            new_name = input()
            if new_name in contestant_list:
                print("Please choose a unique name. No repeated names allowed")
                i-=1
            else:
                contestant_list.append(new_name)
                if len(contestant_list) == turtle_count:
                    picking_names = False
            i+=1

    renaming = True
    while renaming:
        print("The names of the racers are:", end="\n")
        for x in range(len(contestant_list)):
            print(str(x + 1) + ".", contestant_list[x])
        print("Would you like to rename any of them? Y/N")
        valid, renaming_bool = confirmation(input())
        if valid:
            if renaming_bool:
                picking_renaming_subject = True
                while picking_renaming_subject:
                    print()
                    for x in range(len(contestant_list)):
                        print(str(x + 1) + ".", contestant_list[x])
                    print("Which one would you like to rename? Input the racer number. Input 0 if renaming is no "
                          "longer desired.")

                    renaming_specific = input()
                    if integer_check(renaming_specific):
                        renaming_specific = int(renaming_specific)
                        if (renaming_specific < 0) or (renaming_specific > len(contestant_list)):
                            print("Please input a valid number.")
                        elif renaming_specific == 0:
                            print("Moving onto the next phase...")
                            renaming = False
                            picking_names = False
                            creating = False
                            picking_renaming_subject = False
                        else:
                            duplicate = True
                            while duplicate:
                                print("To what would you like to rename racer #" + str(renaming_specific) + "?")
                                new_rename = input()
                                if new_rename in contestant_list:
                                    print("Please choose a new, unique name. No repeated names allowed")
                                else:
                                    contestant_list[renaming_specific-1] = new_rename
                                    duplicate = False

                    else:
                        print("Please put in a valid integer.")
            else:
                renaming = False
                picking_names = False
                creating = False
        else:
            print("Please enter a valid input.")

    turtle_list = []
    for contestant in contestant_list:
        turtle_list.append(trt.Turtle())

    coloring = True

    while coloring:
        print("Would you like to use the default colors for the turtles(recommended)? Y/N")
        colors_valid, colors_bool = confirmation(input())
        if valid:
            default_colors = ["green", "red", "purple", "yellow", "blue", "brown", "pink", "orange", "black", "peru"]
            if colors_bool:
                for i in range(len(turtle_list)):
                    turtle_list[i].color(default_colors.pop(0))

            else:
                default_colors, contestant_list, turtle_list = choose_color(default_colors, contestant_list,
                                                                            turtle_list, False, 0)

        fixing_color = True
        while fixing_color:
            print("So far here is the list of contestants:")
            for i in range(len(contestant_list)):
                print(str(i + 1) + ". " + contestant_list[i] + " - " + str(turtle_list[i].pencolor()))

            print("Would you like to change any of the contestants colors? Y/N")
            change_colors_valid, change_colors_bool = confirmation(input())

            if change_colors_valid:
                if change_colors_bool:
                    print("Which contestant would you like to change? Use the number")
                    change_contestant = input()

                    if integer_check(change_contestant):
                        change_contestant = int(change_contestant)
                        if change_contestant < 1 or change_contestant > len(contestant_list):
                            print("Please input a valid answer.")
                        else:
                            default_colors, contestant_list, turtle_list = choose_color(default_colors, contestant_list,
                                                                                        turtle_list, True,
                                                                                        change_contestant - 1)
                    else:
                        print("Please input a valid answer.")


                else:
                    coloring = False
                    fixing_color = False

            else:
                print("Please input a valid answer.")

    for racer in turtle_list:
        racer.shape("turtle")
        racer.speed(12)

ready = False
while not ready:
    print("Are you ready to start racing? Y/N")
    valid, ready_to_race_bool = confirmation(input())
    if valid:
        if ready_to_race_bool:
            ready=True
        else:
            print("We will start whenever you want. ")
    else:
        print("Please enter a valid input. Choose Y/N")


make_board()
# race phase


trt.done()

# Made By Lance Jodie Salvanera Abuan
# Last Updated: August 9th, 2020, 2:31 PM
