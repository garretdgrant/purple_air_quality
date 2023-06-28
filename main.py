""" This program obtains the users name and greets them. """


def main():
    """ Obtain user's name and greet user. """
    user_name = input("Please enter your name: ")
    print(f'Hi {user_name}, welcome to the Air Quality database.')


if __name__ == '__main__':
    main()

"""
--- sample run #1 ---
Please enter your name: Garret
Hi Garret, welcome to the Air Quality database.

--- sample run #2 ---
Please enter your name: Eric
Hi Eric, welcome to the Air Quality database.
"""
