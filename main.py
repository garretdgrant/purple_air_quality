""" This program obtains the user's name, greets them, displays a simple
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
        print("Please enter a number only!\n")
        print_menu()
        user_input = get_menu_option()
    return user_input


def menu():
    """ Call print_menu and get validated menu choice from user."""
    valid_options = {1: "one", 2: "two", 3: "three", 4: "four",
                     5: "five", 9: "nine"}
    while True:
        print_menu()
        option = get_menu_option()
        if option == 9:
            print("Goodbye!  Thank you for using the database")
            break
        elif option in valid_options:
            print(f"Option {valid_options[option]} is not available yet")
            print()  # new line
        else:
            print("That's not a valid selection\n")


def main():
    """ Obtain user's name and greet user. """
    user_name = input("Please enter your name: ")
    print(f'Hi {user_name}, welcome to the Air Quality database.\n')
    menu()


if __name__ == '__main__':
    main()

"""
Please enter your name: Garret
Hi Garret, welcome to the Air Quality database.

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? Hello
Please enter a number only!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? World
Please enter a number only!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 1
Option one is not available yet

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 2
Option two is not available yet

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 4
Option four is not available yet

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 5
Option five is not available yet

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 10
That's not a valid selection

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What is your choice? 9
Goodbye!  Thank you for using the database

Process finished with exit code 0
"""
