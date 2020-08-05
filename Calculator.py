def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mul(x,y):
    return (x*y)
def div(x,y):
    return (x/y)

CalculatorOn=True
result_continued = False

print("Welcome to a basic calculator!")
# The entire calculator runs off of a while loop so the user can exit whenever they want.
# This is made just in case I wish to add a GUI to this program.
while CalculatorOn:
    print("What would you like to do?")
    print("0. Turn off the calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Input: ", end="")

    # These booleans will be used to prevent issues with invalid inputs.
    choice_valid = False
    numbers_valid = False
    continue_valid = False

    # This while loop is used until the user inputs a valid operation selection to avoid any unnecessary errors.
    while not choice_valid:
        choice = input()
        print("")

        # This is to see if we can move on to doing the calculations.
        if choice in ('1','2','3','4'):
            choice_valid = True
        elif choice == "0":
            break
        else:
            # The latter half of "Invalid Input" is so if there's errors in the future, I can tell where it came from.
            print("Invalid Input of Operation")
            print("Please Input a valid selection.")
    if choice == "0":
        print("Thank you for using my Calculator!")
        break

    # When we know that the user wants to do a VALID operation we  begin asking for what numbers they would like to use.
    while not numbers_valid:
        if result_continued:
            print("Number 1 is",num1)
            num1=str(num1)
        else:
            print("Please enter number 1:")
            num1 = input()
        print("Please enter number 2:")
        num2 = input()

        # Checks if num1 and num2 are actually numbers
        if num1.replace(".","").replace("-","").isnumeric() and num2.replace(".","").replace("-","").isnumeric():
            num1 = float(num1)
            num2 = float(num2)
            numbers_valid = True
        else:
            print("Please enter real numbers.")

    # These calculations can operate without fear of error because of the safety net set up by the previous two while loops
    choice = int(choice)
    if choice == 1:
        answer = add(num1, num2)
        print(num1, "+", num2, "=", answer)
    elif choice == 2:
        answer = sub(num1, num2)
        print(num1, "-" , num2, "=", answer)
    elif choice == 3:
        answer = mul(num1, num2)
        print(num1, "*", num2, "=", answer)
    else:
        answer = div(num1, num2)
        print(num1, "/", num2, "=", answer)

    # This is a loop that lets the user decide if they would like to continue using the result garnered during the above
    #  calculations.
    # This is an idea inspired by physical calculators.
    # This loop is like the previous two safety loops above, it doesn't let the user escape the loop until a valid input
    #   is entered to prevent future errors.
    while not continue_valid:
        print("Would you like to continue using the result?")
        print("1. Yes")
        print("2. No")
        cont = input()
        if cont in ("1", "2"):
            if cont == "1":
                num1 = answer
                result_continued = True
            else:
                result_continued = False

            continue_valid = True
        else:
            # The latter half of "Invalid Input" is so if there's errors in the future, I can tell where it came from
            print("Invalid Input of Continuation")

        # A spacer to make the console less crowded and improve QOL of the user
        print("")


# Made By Lance Jodie Salvanera Abuan
# Last Updated: August 1st, 2020, 9:48 AM