# This program checks if a user has enough money for a trip.

name = input("What is your name? ")
budget = float(input("What is your travel budget? "))
minimum_budget = 1000

print(name, "has a travel budget of $", budget)

if budget >= minimum_budget:
    print("You have enough money for the trip!")
else:
    print("You should save more money for the trip.")
