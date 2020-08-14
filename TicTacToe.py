# This code will be used to create the game Tic-Tac-Toe in an ASCII format
import turtle
import math

# TODO get rid of this comment

# turtle will be used to draw the board and refresh the screen
# I'm sure there's a better library to use for this but i'm not too well versed in all of the available ones

# I used multiple global variables because these will be used to check conditions that impact the entire portion of the
# game.

initial_player = True
player_1_turn = True
board_dimension = 600
game_over = False
reset = None
board = []
player_1_wins = 0
player_2_wins = 0
winner = None

"""
 This is the main function. In order to make it an option for the user to reset the game, at the end
 this program calls a blank version of itself. Also, after every match, the first player alternates. For example,
 if X moves first one round, the next round O moves first. This is for competitive balance, tee-hee!
"""


def make_board(finished):
    global initial_player
    """ "game_over" and "finished" are two separate variables for a reason. game_over is global because it will be used 
        in the function "place_mark()". For some reason the turtle.onscreenclick() can only pass 2 parameters, the x and 
        y coordinates of the cursor. Because of that, I can't signal inside "place_mark()" that the game is over, so 
        instead I pass the game_over variable. game_over and finished should always have the same value.
    """
    global game_over
    global winner
    winner = None
    game_over = False

    # board will be passed between multiple functions so it also must be global
    global board

    # These variables are for appearance.
    # I wanted to print out how many wins each player has on the screen, and in order to keep count they must be global.
    global player_1_wins
    global player_2_wins

    """ This variable switches during the match whereas its counter part "inital_player" switches after the match. This
        is to consistently alternate between players.
    """
    global player_1_turn

    """ The variable "initial_player" is used to determine who goes first. The game doesn't actually start being
        calculated until the "while not finished" loop. This beginning part lays the groundwork for the upcoming, 
        heart racing, tic-tac-toe showdown.
    """

    player_1_turn = initial_player

    # To calculate the actual game, we have an under the cover list that mimics the GUI presented
    # The GUI is purely visual, in my limited knowledge I don't know how to connect the visuals and the code simply
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""], ]

    # This little guy, drawer, is responsible for drawing the board so give him a round of applause!
    drawer = turtle.Turtle()
    drawer.shape("blank")
    drawer.penup()

    wn = turtle.Screen()
    wn.tracer(0)
    # This is to force the tic-tac-toe window to the top of the screen. I do it simply because I like it.
    rootwindow = wn.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    # This tidbit of code prints out how many wins each player has! Super Cute QOL improvement if I say so myself.
    drawer.setposition(-400, -350)
    drawer.write("Player 1 Wins: {}".format(player_1_wins), font=("Arial", 20, "normal"))
    drawer.setposition(-400, -400)
    drawer.write("Player 2 Wins: {}".format(player_2_wins), font=("Arial", 20, "normal"))

    # This while not loop processes the actual game.
    while not finished:

        # To preserve clarity in this code, I made the board drawing into 2 functions! They use the turtle "drawer"
        draw_columns(drawer)
        draw_rows(drawer)

        # The screen refreshes constantly, think of it like FPS! I wonder if I could make an FPS counter for fun...
        wn.update()

        # Now, if the global variable game_over has been changed by one of the functions, then it needs to print that
        # someone has one, and it prints whoever won
        if game_over:
            drawer.setpos(-400, 375)
            drawer.write("Game over!")
            drawer.setpos(-400, 350)

            # winner, a global variable, is changed in the place_mark() function. It has 3 possible values,
            # "X", "O", and "None"

            # each of these if brackets has the same function, write who wins, add one to the win count, and say the
            # game is finished
            if winner == "X":
                drawer.write("The winner is Player 1")
                player_1_wins += 1
                finished = True
            elif winner == "O":
                drawer.write("The winner is Player 2")
                player_2_wins += 1
                finished = True
            else:
                drawer.write("Tie game!")
                finished = True

            # after it prints who won, the code begins prepping to reset the screen.
            # it makes a turtle called "restart_game" which tells the users how to reset
            wn.update()
            restart_game = turtle.Turtle()
            restart_game.shape("blank")
            restart_game.penup()
            restart_game.setposition(-400, 325)
            restart_game.pendown()
            restart_game.write("Click the screen if you would like to reset the game.", align="left")
            restart_game.penup()

        # Whenever the player clicks anywhere on the screen, the "placemark()" function runs
        turtle.onscreenclick(place_mark, 1)


# The name should be self explanatory as to what this function is for
def check_game_complete():
    # calls the global board variable. I stated earlier that the board variable is an array that updates with the GUI.
    # it is an exact replica of the GUI board state in ascii version.
    global board

    # just declaring variables
    victor = None
    game_complete = False

    # the reason I have "not game_complete" is because these functions update the value
    # If the game ends because someone won in a row victory, it might be overriden by a function below it
    # row victory checker
    if not game_complete:
        victor, game_complete = check_row()

    # column victory checker
    if not game_complete:
        victor, game_complete = check_columns()

    # diagonal victory checker
    if not game_complete:
        victor, game_complete = check_diagonals()

    # this checks if there's no blank spots in the board. if there is and a victor hasn't been decided above,
    # then the game will be declared as a tie!
    if "" not in board[0] and "" not in board[1] and "" not in board[2] and not game_complete:
        victor, game_complete = None, True

    return victor, game_complete


# this function checks for row victory
def check_row():
    global board

    for row in board:
        # This checks if an entire row is X's or O's, and if any one of them is, it instantly returns that
        # there is a winner
        if "X" in row and "O" not in row and "" not in row:
            return "X", True
        elif "O" in row and "X" not in row and "" not in row:
            return "O", True

    # if it loops through the whole board and doesn't find a row victor, it does nothing and goes next
    return None, False


# this function checks for column victory
def check_columns():
    global board

    # this "made_column" list will be used to represent each column
    made_column = []

    # This for loop goes between each column
    for column in range(3):

        # This for loop makes a new list to represent each column and the values in each column
        for row in range(3):
            made_column.append(board[row][column])

        # checks to see if the column has is completely X or O and if it is it returns a victor and that the game is
        # over
        if "X" in made_column and "O" not in made_column and "" not in made_column:
            return "X", True
        elif "O" in made_column and "X" not in made_column and "" not in made_column:
            return "O", True

        made_column = []

    # If no column is completely X or O, it returns no victor and that the game is incomplete
    return None, False


# this function checks for diagonal victory
def check_diagonals():
    global board

    diagonal = [board[0][0], board[1][1], board[2][2]]
    # I just hardcoded the top left to bottom right diagonal, no point in making it automated or flexible
    # Checks if someone has conquered a diagonal and if they did return who it was and the game is over
    if "X" in diagonal and "O" not in diagonal and "" not in diagonal:
        return "X", True
    elif "O" in diagonal and "X" not in diagonal and "" not in diagonal:
        return "O", True

    # empty the list to make a new one
    diagonal = [board[2][0], board[1][1], board[0][2]]
    # I just hardcoded the top left to bottom right diagonal, no point in making it automated or flexible
    # Checks if someone has conquered a diagonal and if they did return who it was and the game is over
    if "X" in diagonal and "O" not in diagonal and "" not in diagonal:
        return "X", True
    elif "O" in diagonal and "X" not in diagonal and "" not in diagonal:
        return "O", True

    # If no one has conquered a diagonal then games not over and there's no winner
    return None, False


# this function places the x's or o's and checks if the game is complete
def place_mark(x, y):
    # calls the overarching variables
    global initial_player
    global player_1_turn
    global game_over
    global winner

    # this turtle will be drawing each of the shapes!!!!
    turtle.penup()
    turtle.shape("blank")
    turtle.setpos(x, y)

    # now if the player has clicked and the game isn't over they draw
    if not game_over:
        # this checks who's turn it is
        if player_1_turn:
            # This variable "valid" is important because if the player clicks in an invalid spot, then the turns don't
            # swap. So if they click somewhere valid, it returns that they clicked somewhere valid, and then
            # player_1_turn becomes false.
            valid = draw_x(x, y)
            player_1_turn = not valid

        else:

            # Does the same thing as above but for player two instead of player one. Because it's player two, we want
            # to make valid do the opposite thing as above. If they do a valid turn, it becomes player ones turn.
            valid = draw_o(x, y)
            player_1_turn = valid

    # if the player clicks and the game is over that means they want to reset!
    else:
        # This else is for whenever the game is over.
        # It changes who the alternate player is, says it's resetting, then calls make_board().
        initial_player = not initial_player
        print("Resetting!")
        turtle.clearscreen()
        make_board(False)

    # updates the global variables
    winner, game_over = check_game_complete()


# this returns which column the cursor was in using the xcor
def which_column(xcor):
    if -300 <= xcor <= -100:
        column = 0
    elif -100 < xcor <= 100:
        column = 1
    elif 100 < xcor < 300:
        column = 2
    else:
        column = -1
    return column


# this returns which row the cursor was in using the ycor
def which_row(ycor):
    if 100 <= ycor <= 300:
        row = 0
    elif 100 > ycor >= -100:
        row = 1
    elif -100 > ycor >= -300:
        row = 2
    else:
        row = -1
    return row


# This function calls which_column and which_row and uses that to determine drawing location
def draw_x(xcor, ycor):
    global board

    # "shape_drawer" turtle draws the shape
    shape_drawer = turtle.Turtle()
    shape_drawer.penup()
    shape_drawer.shape("blank")

    row = which_row(ycor)
    column = which_column(xcor)

    # -1 indicates an invalid location. If the location is valid and the spot is empty then draw the X
    if row != -1 and column != -1 and board[row][column] == "":

        # this is to draw the X. I'm sure it could be prettier but... this is good for now
        shape_drawer.setpos(-200 + column * 200, 200 - row * 200)
        shape_drawer.pendown()
        shape_drawer.pensize(10)
        shape_drawer.setheading(315)
        shape_drawer.forward(math.sqrt(95 ** 2 + 95 ** 2))
        shape_drawer.setheading(135)
        shape_drawer.forward(2 * math.sqrt(95 ** 2 + 95 ** 2))
        shape_drawer.setpos(-200 + column * 200, 200 - row * 200)
        shape_drawer.pendown()
        shape_drawer.pensize(10)
        shape_drawer.setheading(45)
        shape_drawer.forward(math.sqrt(95 ** 2 + 95 ** 2))
        shape_drawer.setheading(225)
        shape_drawer.forward(2 * math.sqrt(95 ** 2 + 95 ** 2))

        # updates the board global variable
        board[row][column] = "X"

        proper_spot = True
    else:
        # if they didn't click in a proper spot or the spot they clicked on was occupied, then it says to try again
        print("Please click a valid area.")
        proper_spot = False

    return proper_spot


# This function calls which_column and which_row and uses that to determine drawing location
def draw_o(xcor, ycor):
    global board

    # "shape_drawer" turtle draws the shape
    shape_drawer = turtle.Turtle()
    shape_drawer.penup()
    shape_drawer.shape("blank")

    row = which_row(ycor)
    column = which_column(xcor)

    # -1 indicates an invalid location. If the location is valid and the spot is empty then draw the O
    if row != -1 and column != -1 and board[row][column] == "":
        shape_drawer.setpos(-200 + column * 200, 100 - row * 200)
        shape_drawer.pendown()
        shape_drawer.pensize(10)
        shape_drawer.circle(100)

        # updates board variable
        board[row][column] = "O"
        proper_spot = True
    else:

        # if they didn't click in a proper spot or the spot they clicked on was occupied, then it says to try again
        proper_spot = False
        print("Please click a valid area.")

    return proper_spot

    # YLINES = -150,150
    # XLINES = -150, 150


# this just draws the vertical lines, nothing computational
def draw_columns(pencil):
    pencil.penup()
    for i in range(2):
        pencil.setposition(-100 + (board_dimension / 3) * i, 300)
        pencil.setheading(270)
        pencil.pendown()
        pencil.forward(board_dimension)
        pencil.penup()


# this just draws the horizontal lines, nothing computational
def draw_rows(pencil):
    pencil.penup()
    for i in range(2):
        pencil.setposition(-300, -100 + (board_dimension / 3) * i)
        pencil.setheading(0)
        pencil.pendown()
        pencil.forward(board_dimension)
        pencil.penup()


# Begins the game!
make_board(False)

turtle.mainloop()

# Made By Lance Jodie Salvanera Abuan
# Last Updated: August 14th, 2020, 2:32 PM