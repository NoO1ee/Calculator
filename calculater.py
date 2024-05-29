import os
import time
import math
clear = lambda: os.system('cls')
from getkey import getkey, keys

def menu():

    print("Welcome to my calculator")

    #Creating a menu
    menuOptions = ["Multiply", "Divide", "Subtraction", "Addition", "Square root", "Elevate", "Percentage", "Pythagorean Theorem", "8", "Exit"]
    menuSelected = 0
    end_program = False

    while not end_program:
        print('\x1b[?25l')
        clear()

        if menuSelected == 0:
            print("\t[ " + menuOptions[0] + " ]" + "\t<--")
            print(menuOptions[1])
            print(menuOptions[2])
            print(menuOptions[3])
            print(menuOptions[4])
            print(menuOptions[5])
            print(menuOptions[6])
            print(menuOptions[7])
            print(menuOptions[7])
            print(menuOptions[8])
            print(menuOptions[9])
        
        elif menuSelected == 1:
            print(menuOptions[0])
            print("\t[ " + menuOptions[1] + " ]" + "\t<--")
            print(menuOptions[2])
            print(menuOptions[3])
            print(menuOptions[4])
            print(menuOptions[5])
            print(menuOptions[6])
            print(menuOptions[7])
            print(menuOptions[7])
            print(menuOptions[8])
            print(menuOptions[9])

        elif menuSelected == 2:
            print(menuOptions[0])
            print(menuOptions[1])
            print("\t[ " + menuOptions[2] + " ]" + "\t<--")
            print(menuOptions[3])
            print(menuOptions[4])
            print(menuOptions[5])
            print(menuOptions[6])
            print(menuOptions[7])
            print(menuOptions[8])
            print(menuOptions[9])


        elif menuSelected == 3:
            print(menuOptions[0])
            print(menuOptions[1])
            print(menuOptions[2])
            print("\t[ " + menuOptions[3] + " ]" + "\t<--")
            print(menuOptions[4])
            print(menuOptions[5])
            print(menuOptions[6])
            print(menuOptions[7])
            print(menuOptions[8])
            print(menuOptions[9])


        elif menuSelected == 4:
            print(menuOptions[0])
            print(menuOptions[1])
            print(menuOptions[2])
            print(menuOptions[3])
            print("\t[ " + menuOptions[4] + " ]" + "\t<--")
            print(menuOptions[5])
            print(menuOptions[6])
            print(menuOptions[7])
            print(menuOptions[8])
            print(menuOptions[9])


        elif menuSelected == 5:
            print(menuOptions[0])
            print(menuOptions[1])
            print(menuOptions[2])
            print(menuOptions[3])
            print(menuOptions[4])
            print("\t[ " + menuOptions[5] + " ]" + "\t<--")
            print(menuOptions[6])
            print(menuOptions[7])
            print(menuOptions[8])
            print(menuOptions[9])


        elif menuSelected == 6:
            print(menuOptions[0])
            print(menuOptions[1])
            print(menuOptions[2])
            print(menuOptions[3])
            print(menuOptions[4])
            print(menuOptions[5])
            print("\t[ " + menuOptions[6] + " ]" + "\t<--")
            print(menuOptions[7])
            print(menuOptions[8])
            print(menuOptions[9])


        elif menuSelected == 7:
            print(menuOptions[0])
            print(menuOptions[1])
            print(menuOptions[2])
            print(menuOptions[3])
            print(menuOptions[4])
            print(menuOptions[5])
            print(menuOptions[6])
            print("\t[ " + menuOptions[7] + " ]" + "\t<--")
            print(menuOptions[8])
            print(menuOptions[9])

        elif menuSelected == 8:
            print(menuOptions[0])
            print(menuOptions[1])
            print(menuOptions[2])
            print(menuOptions[3])
            print(menuOptions[4])
            print(menuOptions[5])
            print(menuOptions[6])
            print(menuOptions[7])
            print("\t[ " + menuOptions[8] + " ]" + "\t<--")
            print(menuOptions[9])

        elif menuSelected == 9:
            print(menuOptions[0])
            print(menuOptions[1])
            print(menuOptions[2])
            print(menuOptions[3])
            print(menuOptions[4])
            print(menuOptions[5])
            print(menuOptions[6])
            print(menuOptions[7])
            print(menuOptions[8])
            print("\t[ " + menuOptions[9] + " ]" + "\t<--")

        keyPressed = getkey()

        if keyPressed == keys.DOWN and menuSelected + 1 != len(menuOptions):
            menuSelected += 1
        elif keyPressed == keys.UP and menuSelected >= 1:
            menuSelected -= 1
        elif keyPressed == keys.ENTER:
            if menuSelected == 0:
                multiply(menu)
            elif menuSelected == 1:
                divide(menu)
            elif menuSelected == 2:
                subtraction(menu)
            elif menuSelected == 3:
                addition(menu)
            elif menuSelected == 4:
                square_root(menu)
            elif menuSelected == 5:
                elevated(menu)
            elif menuSelected == 6:
                percentage(menu)
            elif menuSelected == 7:
                pythagorean_theorem(menu)
            elif menuSelected == 8:
                #FUNCTION
                print("9")
            elif menuSelected == 9:
                #FUNCTION AVSLUTA PROGRAM
                print("9")
                end_program = True
                clear()
                print("Thank you for using the calculator!")
                input("Press Enter to exit!")
                print('\x1b[?25h')



def multiply(prev_func):
    clear()
    print("Multiplier: \nType in the two numbers you want to multiply.")
    
    try:
        get_usr = float(input("Number 1: "))
        get_usr_mlt = float(input("Number 2: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        input("Press Enter to try again")
        return(multiply(prev_func))
    
    multiply_num = get_usr * get_usr_mlt

    clear()
    print("You entered:", get_usr, "multiply", get_usr_mlt)
    print("\nResult: ", multiply_num)
    input("Press Enter")
    options(multiply, prev_func)

def divide(prev_func):
    clear()
    print("Divider: \n Type in the two numbers you want to divide.")

    try:
        get_div_num = float(input("Number 1: "))
        get_div_num2 = float(input("Number 2: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        input("Press Enter to try again.")
        return(divide(prev_func))
    
    divide_usr_num = get_div_num / get_div_num2

    clear()
    print("You entered: ", get_div_num, "divide ", get_div_num2)
    print("\nResult: ", divide_usr_num)
    input("Press Enter")
    options(divide, prev_func)

def subtraction(prev_func):
    clear()
    print("Subtraction: \n Type in the two numbers you want to subtract.")

    try:
        get_sub_num = float(input("Number 1: "))
        get_sub_num2 = float(input("Number 2: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return(subtraction(prev_func))
    
    subtract_usr_num = get_sub_num - get_sub_num2

    clear()
    print("You entered: ", get_sub_num, "subtract ", get_sub_num2)
    print("\nResult: ", subtract_usr_num)
    input("Press Enter")
    options(subtraction, prev_func)
    
def addition(prev_func):
    clear()
    print("Addition: \n Type in the two numbers you want to add.")

    try:
        get_add_num = float(input("Number 1: "))
        get_add_num2 = float(input("Number 2: "))
    except ValueError:
        clear()
        print("Invalid input. Please enter numeric values.")
        input("Press Enter to try again")
        return(addition(prev_func))
    
    add_usr_num = get_add_num + get_add_num2

    clear()
    print("You entered: ", get_add_num, "add ", get_add_num2)
    print("\nResult: ", add_usr_num)
    input("Press Enter")
    options(addition, prev_func)

def square_root(prev_func):
    clear()
    print("Square root: \n Type in the one number you want to know the Square root of.")

    try:
        get_sqr_num = abs(float(input("Number : ")))
    except ValueError:
        clear()
        print("Invalid input. Please enter numeric values.")
        input("Press Enter to try again")
        return(square_root(prev_func))
    
    sqr_usr = math.sqrt(get_sqr_num)

    clear()
    print("You entered: ", get_sqr_num)
    print("\nResult: ", sqr_usr)
    round_off_sqr = math.floor(sqr_usr)
    print("\nResult round off: ", round_off_sqr)
    input("Press Enter")
    options(square_root, prev_func)

def elevated(prev_func):
    clear()
    print("Elevated: \n Type in the first number and the elevate with the second number.")

    try:
        get_main_num = float(input("Number: "))
        get_elv_num = float(input("Elevate Number: "))
    except ValueError:
        clear()
        print("Invalid input. Please enter numeric values.")
        input("Press Enter to try again")
        return(elevated(prev_func))
    
    elevate_usr = get_main_num ** get_elv_num
    clear()
    print("You entered: ", get_main_num, "and elevated with ", get_elv_num)
    print("\nResult: ", elevate_usr)
    round_off_el = math.floor(elevate_usr)
    print("Round off result: ", round_off_el)
    input("Press Enter")
    options(elevated, prev_func)

def percentage(prev_func):
    clear()
    print("Percentage: This takes the value and takes the percentage of")

    try:
        print("Type in first number and second number for percentage off.")
        per_usr_main = float(input("\nNumber: "))
        per_off_main = float(input("Percentage: "))
    except ValueError:
        clear()
        print("Invalid input. Please enter numeric values.")
        input("Press Enter to try again")
        return(percentage(prev_func))
    

    percentage_value = ((per_off_main / 100) * per_usr_main)
    percentage_tot = per_usr_main - percentage_value
    clear()
    print("You entered: ", per_usr_main, " and took the percentage off: ", per_off_main)
    print("\nResult: ", percentage_value)
    print("\nYou have total left: ", percentage_tot)
    input("Press Enter")
    options(percentage, prev_func)

def pythagorean_theorem(prev_func):
    clear()
    print("Pythagorean theorem: Calculates the two values that you have and gives you the answer.")

    try:
        get_1st_py = float(input("First Number: "))
        get_2nd_py = float(input("Second Number: "))
    except ValueError:
        clear()
        print("Invalid input. Please enter numeric values.")
        input("Press Enter to try again")
        return(pythagorean_theorem(prev_func))
    
    convert_1st = get_1st_py ** 2
    convert_2nd = get_2nd_py ** 2

    









## Menu options

def options(prev_func, menu_func):
    clear()
    print("\nType 'Y' to redo or 'N' to go back to menu")
    choice = str(input("Y/N: "))

    if choice == "Y" or choice == "y":
        clear()
        print("Reloading...")
        time.sleep(1)
        prev_func(menu_func)
    elif choice == "N" or choice == "n":
        clear()
        print("Exiting")
        time.sleep(1)
        back(menu_func)
    elif choice != "N" or choice != "n" or choice != "Y" or choice != "y":
        clear()
        print("Wrong input.")
        print("Taking you back to menu.")
        time.sleep(2)
        back(menu_func)
    else:
        clear()
        print("Wrong input.")
        print("Taking you back to menu.")
        time.sleep(2)
        back(menu_func)

def back(menu_func):
    clear()
    print("Getting you back to the menu...")
    time.sleep(2)
    clear()
    print("One moment...")
    time.sleep(2)
    menu_func()



# To start
menu()