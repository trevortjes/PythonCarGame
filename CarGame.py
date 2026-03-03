import tkinter as tk
from time import sleep

waittime = 0.1 # New line speed
initialBudget = 100000

# Stats of the player
class user(object):
    def __init__(self, name, budget, inventory):
        self.name = name
        self.budget = budget

    def display_info(self):
        return f"Hi {self.name}, you have a budget of ${self.budget}"

    def __str__(self):
        return self.display_info()

# stats of the cars
class vehicle(object):
    def __init__(self, brand, type, horsepower, price):
        self.brand = brand # always porsche
        self.type = type
        self.horsepower = horsepower # "how good is the car for racing"
        self.price = price # New price

# stats of the owned car
class ownedcar(object):
    def __init__(self, brand, type, horsepower, value):
        self.brand = brand
        self.type = type
        self.horsepower = horsepower
        self.value = value # Price after buying

    def display_info(self):
        return f"You own a {self.brand} {self.type} with {self.horsepower} horsepower and a remaining value of ${self.value}"

    def __str__(self):
        return self.display_info()

#player information
user0 = user("Poepman", initialBudget, 0)
ownedcar0 = ownedcar("0","0", 0, 0)
ownedlist = [ownedcar0]

#available cars
car0 = vehicle('Porsche', '914', 98, 2500)
car1 = vehicle('Porsche', '944 Turbo', 120, 14000)
car2 = vehicle('Porsche', '911 Carrera S', 205, 25000)
car3 = vehicle('Porsche', '356 Speedster', 65, 66000)
carlist = [car0, car1, car2, car3]

#Plays once at start of game to get name and introduce
def introduction():
    print(user0)
    print(ownedcar0)
    print("Driver, enter your name")
    #user0.name = input(">")
    print("Hello " + user0.name)
    sleep(waittime)
    print("Welcome to the world of racing")
    sleep(waittime)
    print("Your current budget is $" + str(user0.budget))
    sleep(waittime)
    print("Use it to buy your first car")
    sleep(waittime)

#Main location, can go everywhere from here and check your stats
def home():
    print(user0)
    print(ownedcar0)

#Buying a car
def dealer():

    print("Welcome to our Porsche dealer " + user0.name)
    sleep(waittime)
    choicemade = 0

    while(choicemade == 0):

        print("Buy one of these cars if it fits your budget:")

        for index, x in enumerate(carlist):
            print("[" + str(index) + "] " + x.brand + " " + x.type + " Horsepower: " + str(x.horsepower) + " Price: " + str(x.price))
            sleep(waittime)


        carchoice = int(input(">"))
        if carlist[carchoice].price > user0.budget:
            print("You're too poor for that one")
        else:
            print("Do you want to buy " + carlist[carchoice].brand + " " + carlist[carchoice].type + " for " + str(carlist[carchoice].price) + "? [Y/N]")

            choice = input(">")

            if choice == "Y" or choice == "y":
                choicemade = 1
                #user0.inventory.append(carlist[carchoice])
                ownedcar0.brand = carlist[carchoice].brand
                ownedcar0.type = carlist[carchoice].type
                ownedcar0.horsepower = carlist[carchoice].horsepower
                ownedcar0.value = carlist[carchoice].price * 0.8
                user0.budget -= carlist[carchoice].price
                #add car to garage
            else:
                print("Leave dealer? [Y/N]")
                leave = input(">")
                if leave == "Y" or leave == "y":
                    choicemade = 1
                else:

                  pass

    home()



introduction()
dealer()
