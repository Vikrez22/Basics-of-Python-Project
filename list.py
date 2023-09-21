# Who will pay the bill

import random

# test_seed = int(input("Create a seed number: "))
# (random.seed(test_seed))

namesAsCSV = input("Give me everybody's names, seperated by a comma.\n")
names = namesAsCSV.split(",")
# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

# print(f"{} is going to buy the meal")