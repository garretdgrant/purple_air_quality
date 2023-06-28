""" This program obtains the users name, greets them, displays a simple
menu, and gets a menu option from the user. The program uses a try
except block to validate user input.
"""


def print_menu():
    """ Print the menu to the user."""
    print("""Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit""")


def get_menu_option():
    """ Get validated menu option from the user."""
    try:
        user_input = int(input("What is your choice? "))
    except ValueError:
        print("\nPlease enter a number only!")
        print_menu()
        user_input = get_menu_option()
    return user_input


def menu():
    """ Call print_menu and get menu choice from user."""
    print_menu()
    user_choice = get_menu_option()
    print(user_choice)


def main():
    """ Obtain user's name and greet user. """
    user_name = input("Please enter your name: ")
    print(f'Hi {user_name}, welcome to the Air Quality database.\n')
    menu()


if __name__ == '__main__':
    main()

"""
--- Note --- 
I added an extra feature so the program does not
exit until the user enters an integer. 
I used recursion to accomplish this
in get_menu_option()

--- sample run (Invalid and Valid Respectively) ---
Please enter your name: Garret
Hi Garret, welcome to the Air Quality database.

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit

What is your choice? Hello World (Invalid)
Please enter a number only!
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit

What is your choice? 6
6

Process finished with exit code 0
"""
