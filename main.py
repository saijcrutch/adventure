import random
import choices
# Story of a man trying to get $100 to take a trip

name = input("What do you want your character's name to be? ")
intro = print(f"This story is about you, {name}, and your quest to get $100 to go on vacation.")

def adventure():
    search = choices.search_choice

    intro2 = print("You're not gonna go on vacation by laying in bed. Time to get up and make some money!")
    user = input(f"Do you want to search {search[0]} (1) or search {search[1]} (2)? ")

    if user == "1":
        print('No callbacks today.')
    elif user == "2":
        print('Yay! You got a job today and made money!')
    
adventure()