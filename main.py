import random
import choices
# Story of a man trying to get $100 to take a trip

days = choices.days
name = input("What do you want your character's name to be? ")
intro = print(f"This story is about you, {name}, and your quest to get $100 to go on vacation.")

def adventure():
    search = choices.search_choice
    
    intro2 = print(f"You're not gonna go on vacation by laying in bed. You only have {money_total()} \
                   in your bank account. Time to get up and make some money!")
    user = input(f"Do you want to {search[0]} (1) or search {search[1]} (2)? ")

def money_total():
    money = 0
    goal = 100

    if days == 0 and money == 0:
        print(f"Somehow you managed to make ${money} this week. Guess you really didn't want to go on vacation.") 
    elif days == 0 and money >= 1:
        print(f"You made ${money} this week. That's enough for a candy bar but not a vacation.") 
    elif days == 0 and money == 100:
        print(f"You actually made ${money}. Go take that vacation. You earned it")
    else:
        print(f"You made ${money}! That's ${money - goal} over your goal. Now you can really treat yourself!!!")

    
adventure()