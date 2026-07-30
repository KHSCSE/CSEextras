import requests

base_url = 'https://cs-api.pltw.org/'
user_name = input("Type your username:")

print("\nWelcome to PLTW.book.CHAT\n")

user_action = ''
possible_actions = "\nG to Get, P to Post, V to Vote, R to Reset, Q to Quit"


# loop while the user does not choose to quit
while user_action != 'Q':
    user_action = input(possible_actions).upper()
    if user_action == 'G':
        pass
        # TODO delete 'pass'
        # copy / paste the code that gets all posts
    elif user_action == 'P':
        pass
        # TODO delete 'pass'
        # copy / paste the code that makes a new post
    elif user_action == 'V':
        pass
        # TODO delete 'pass'
        # copy / paste the code that votes for an item
    elif user_action == 'R':
        pass
        # TODO delete 'pass'
        # write the code that resets the data
    
    
print("\n...exiting the program...")