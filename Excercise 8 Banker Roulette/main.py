# write down names as follows - Angela, Ben, Jenny, Michael, Chloe
names_string = input("Who are willing to pay? ")
names = names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(f"{names[random_choice]} is going to buy meal today.")