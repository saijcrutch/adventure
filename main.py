import random
import choices
# Story of a man trying to get $100 to take a trip

time = 0
goal = 100
days = choices.all_days
name = input("What do you want your character's name to be? ")
intro = print(f"This story is about you, {name}, and your quest to get $100 to go on vacation. You have 1 week.")

def adventure():
    new_day = 7
    job = random.choice(choices.in_person_jobs)
    search = choices.search_choice
    money = 0
    global time
    global days

    print(f"You're not gonna go on vacation by laying in bed. You have ${money} in your bank account so get up and make some money!")
    while new_day > 0:
        user = input(f"Do you want to {search[0]} (1) or search {search[1]} (2)? ")
        if user == "1":
            new_day -= 3
            del choices.week[0:3]
            while True:
                user = input(f"Where do you want to work? {first_item(choices.locations)}? ")
                if user == "1":
                    money += int(len(choices.week[0:3])) * choices.bk_pay
                    print(f"You get a part-time job at {choices.locations[0][0]} for ${choices.bk_pay} a day. \
You work for 3 days and make ${int(len(choices.week[0:3])) * choices.bk_pay}.")
                    print(f"You have {new_day} days left to make ${goal-money}. You currently have ${money}.")
                elif user == "2":
                    money += int(len(choices.week[0:3])) * choices.wmart_pay
                    print(f"You get a part-time job at {choices.locations[1][0]} for ${choices.wmart_pay} a day. \
You work for 3 days and make ${int(len(choices.week[0:3])) * choices.wmart_pay}.")
                    print(f"You have {new_day} days left to make ${goal-money}. You currently have ${money}.")
                elif user == "3":
                    money += int(len(choices.week)) * choices.lowes_pay
                    print(f"You get a part-time job at {choices.locations[2][0]} for ${choices.lowes_pay} a day. \
You work for 3 days and make ${int(len(choices.week)) * choices.lowes_pay}.")
                    print(f"You have {new_day} days left to make ${goal-money}. You currently have ${money}.")
                else:
                    print("Yeah, I know these aren't the best jobs but beggars can't be choosers. Choose again.")
                    continue
                break
        if user == '2':
            del choices.week[0:2]
            randoms = random.randrange(len(choices.neighbors))
            if randoms == 0:
                new_day -= 1
                print("Seems no one needs your services today. It's too late to find anything else now so you might as well \
sleep.") 
                print(f"You have {new_day} days left to make ${goal-money}. You currently have ${money}.")
            else:
                money += randoms * job[1]
                new_day -= 2
                print("There should be some jobs in the neighborhood that you can do. Why don't you ask your \
neighbors if they have any work?")
                print(f"It seems that your neighbor(s) {', '.join(random.sample(choices.neighbors, randoms))} want(s) you to \
{job[0]} for ${job[1]} apiece.")
                print(f"You have {new_day} days left to make ${goal-money}. You currently have ${money}.")
                continue
        if new_day == 1:
            new_day -= 1
            print("Don't stress yourself out before the day of your vacation. Just stay home and watch TV.")
    if new_day <= -1:
        print("You got overzealous trying to save money. All that hard work was for nothing!")
    else:
        money_total(money, goal)
            

def first_item(x):
    count = 0
    list = []
    new_list = []

    for item in x:
        list.append(item[0])

    for item1 in list:
        count += 1
        y = f"{item1} ({count})"
        new_list.append(y)

    return ', '.join(new_list)

def list_append(x):
    count = 0
    list = []

    for item in x:
        count += 1
        y = f"{item} ({count})"
        list.append(y)

    print(', '.join(list))

def money_total(total, goal):
    if goal == 0:
        print(f"Somehow you only managed to make ${total} this week. Guess you really didn't want to go on vacation.") 
    elif goal == 1 and goal <= 99:
        print(f"You made ${total} this week. That's enough for a candy bar but not a vacation.") 
    elif goal == 100:
        print(f"You actually made ${goal}. Go take that vacation. You earned it!")
    else:
        print(f"You made ${total}! That's ${total - goal} over your goal. Now you can really treat yourself!!!")
    
adventure()