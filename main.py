import random
import choices
# Story of a man trying to get $100 to take a trip

days = int(len(choices.days[0])+len(choices.days[1]))
name = input("What do you want your character's name to be? ")
intro = print(f"This story is about you, {name}, and your quest to get $100 to go on vacation. You have 1 week.")

def adventure():
    search = choices.search_choice
    money = 0

    while days > 0:
        intro2 = print(f"You're not gonna go on vacation by laying in bed. You have ${money} \
                    in your bank account so get up and make some money!")
        user = input(f"Do you want to {search[0]} (1) or search {search[1]} (2)? ")
        if user == '1':
            print(f"Where do you want to work? {choices.locations[0][0]}, {choices.locations[1][0]}, {choices.locations[2][0]}")

def money_total():
    money_tot = 0
    goal = 100

    if days == 0 and money_tot == 0:
        print(f"Somehow you managed to make ${money_tot} this week. Guess you really didn't want to go on vacation.") 
    elif days == 0 and money_tot >= 1:
        print(f"You made ${money_tot} this week. That's enough for a candy bar but not a vacation.") 
    elif days == 0 and money_tot == 100:
        print(f"You actually made ${money_tot}. Go take that vacation. You earned it")
    else:
        print(f"You made ${money_tot}! That's ${money_tot - goal} over your goal. Now you can really treat yourself!!!")

def no_of_days(lists):
    count = 0
    for x in lists:
        count += len(lists)
    return count
    

