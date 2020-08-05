import turtle as trt
import random as rd
import math

def confirmation(S):
    if S.lower() == "y" or S.lower() == "n":

        if(S.lower()=="y"):
            answer=True
        else:
            answer=False
        return True, answer

    else:
        return False, None

def makeBoard():
    print("Drawing the board now...")
    drawer = trt.Turtle()

    drawer.penup()
    drawer.setposition(-350, 350)
    drawer.speed(0)

    for i in range(21):
        drawer.pendown()
        drawer.forward(25)
        drawer.write(i)
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
    drawer.setposition(-350,350)

    for i in range(len(contestant_list)):
        turtle_list[i].penup()
        turtle_list[i].setpos(-350,300-i*70)

def chooseColor(color_list,list_of_contestants,list_of_turtles, individual, number):

    if not individual:
        iteration = 0
        while iteration < len(list_of_contestants):
            print("Choose a color(number) for Contestant", list_of_contestants[iteration])

            for j in range(len(color_list)):
                print(str(j + 1) + ".", color_list[j])
            color_choice = input()

            if integerCheck(color_choice):
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
        if integerCheck(ind_color_choice):
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

def integerCheck(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def collision(turtle, steps, list_of_turtles,number):
    safe_path = True
    future_xcor = steps*math.cos(turtle.heading())
    future_ycor = steps*math.sin(turtle.heading())
    collider_list = list_of_turtles.copy()

    del collider_list[number]
    for collider in collider_list:
        obj_xcor = collider.xcor()
        obj_ycor = collider.ycor()
        if (abs(future_xcor-obj_xcor)<20 and abs(future_ycor-obj_ycor)<20):
            safe_path = False
        elif (future_ycor>340 or future_ycor<-240):
            print("Out of bounds!")
            safe_path = False


    return safe_path

def run(turtle,list_of_turtles,iteration):
    init_angle = turtle.heading()
    proper_angle = False
    collision_count=0
    while not proper_angle:
        turtle.setheading(init_angle)
        steps = rd.randint(10, 50)
        if collision_count<5:

            if 10 < turtle.heading() < 30:
                turtle.right(rd.randint(0, 12))
            elif 350 > turtle.heading() > 330:
                turtle.left(rd.randint(0, 12))
            else:
                turtle.right(rd.randint(-12, 12))
            proper_angle = collision(turtle, steps, list_of_turtles, iteration)
            collision_count += 1
        else:
            steps = 0
            proper_angle = True

    turtle.forward(steps)

#This creates the turtles
creating = True
while creating:
    valid_count = False
    while not valid_count:
        print("Hello! Welcome to the turtle race! How many turtles would you like to make?\nMin Amount: 2\nMax Amount: 8")
        turtle_count=input()
        if not integerCheck(turtle_count):
            print("Please enter a valid integer.")
        elif int(turtle_count)<2 or int(turtle_count)>8:
            print("Please enter an integer between 2 and 8")
        else:
            confirmed = False
            turtle_count=int(turtle_count)
            while not confirmed:
                print("You said you want to make",turtle_count,"turtles. Is this true? Y/N")
                valid, count_bool = confirmation(input())
                if valid:
                    valid_count = count_bool
                    print("Moving onto the next phase...")
                    confirmed = True
                else:
                    print("Please enter a valid input.")


    picking_names = True
    while picking_names:
        contestant_list=[]
        print("Please name each turtle.")

        for turt in range(turtle_count):
            print("The name of racer number",turt+1,"is: ")
            contestant_list.append(input())


        renaming = True
        while renaming:
            print("The names of the racers are:", end="\n")
            for x in range(len(contestant_list)):
                print(str(x + 1) + ".", contestant_list[x])
            print("Would you like to rename any of them? Y/N")
            valid, renaming_bool = confirmation(input())
            if valid:
                if renaming_bool:
                    print("Which one would you like to rename? Input the racer number. Input 0 if renaming is no longer desired.")


                    renaming_specific = input()
                    if integerCheck(renaming_specific):
                        renaming_specific = int(renaming_specific)
                        if (renaming_specific < 0) or (renaming_specific > len(contestant_list)):
                            print("Please input a valid number.")
                        elif renaming_specific==0:
                            print("Moving onto the next phase...")
                            renaming = False
                            picking_names = False
                            creating = False
                        else:
                            print("To what would you like to rename racer #"+str(renaming_specific)+"?")
                            contestant_list[renaming_specific-1] = input()

                else:
                    renaming = False
                    picking_names = False
                    creating = False
            else:
                print("Please enter a valid input.")

    turtle_list=[]
    for contestant in contestant_list:
        turtle_list.append(trt.Turtle())

    coloring = True


    while coloring:
        print("Would you like to use the default colors for the turtles(recommended)? Y/N")
        colors_valid, colors_bool = confirmation(input())
        if valid:
            default_colors = ["green", "red", "purple", "yellow", "blue", "brown", "pink", "orange","black", "peru"]
            if colors_bool:
                for i in range(len(turtle_list)):
                    turtle_list[i].color(default_colors.pop(0))

            else:
                default_colors, contestant_list, turtle_list = chooseColor(default_colors, contestant_list, turtle_list,False,0)




        fixing_color=True
        while fixing_color:
            print("So far here is the list of contestants:")
            for i in range(len(contestant_list)):
                print(str(i+1)+". "+contestant_list[i]+ " - " + str(turtle_list[i].pencolor()))

            print("Would you like to change any of the contestants colors? Y/N")
            change_colors_valid, change_colors_bool = confirmation(input())

            if change_colors_valid:
                if change_colors_bool:
                    print("Which contestant would you like to change? Use the number")
                    change_contestant = input()

                    if integerCheck(change_contestant):
                        change_contestant = int(change_contestant)
                        if change_contestant < 1 or change_contestant>len(contestant_list):
                            print("Please input a valid answer.")
                        else:
                            default_colors, contestant_list, turtle_list = chooseColor(default_colors, contestant_list,turtle_list, True, change_contestant-1)
                    else:
                        print("Please input a valid answer.")


                else:
                    coloring=False
                    fixing_color=False

            else:
                print("Please input a valid answer.")

    for racer in turtle_list:
        racer.shape("turtle")

makeBoard()
# race phase
race_incomplete = True
for element in turtle_list:
    element.penup()

while race_incomplete:

    for i in range(len(turtle_list)):
        run(turtle_list[i], turtle_list, i)

    list_of_winners = []

    for i in range(len(turtle_list)):
        if turtle_list[i].xcor() > 175:
            race_incomplete = False
            list_of_winners.append((contestant_list[i], turtle_list[i].pencolor()))

if len(list_of_winners) == 1:
    print("The winner of this race is:")
    for a, b in list_of_winners:
        print(a, "-", b)

elif len(list_of_winners) > 1:
    print("The winners of this race are: ")
    for a,b in list_of_winners:
        print(a,"-",b)

trt.done()

# Made By Lance Jodie Salvanera Abuan
# Last Updated: August 4th, 2020, 2:31 PM