# monty.py

# code Door, Contestant, and MontyHall classes

import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Door:
    def __init__(self, prize = False):
        self.prize = prize
        self.doorOpen = False
        self.image = "images/door.jpg"

    def openDoor(self):
        self.doorOpen = True
        if self.prize:
            self.image = "images/money.jpg"
        else:
            self.image = "images/goat.jpg"

class Contestant:
    def __init__(self):
        self.doorChoice = None
        self.strategy = None

    def chooseStrategy(self, strategy):
        self.strategy = strategy

    def chooseDoor(self, choice):
        self.doorChoice = choice

class MontyHall:
    def __init__(self):
        self.doors = [Door(), Door(), Door()]
        self.doors[random.randint(0, 2)].prize = True
        self.contestant = Contestant()

    def get_choice(self):
        choice = int(input("Choose a Door."))
        self.contestant.chooseDoor(choice)

    def display(self):
        fig, axs = plt.subplots(1, len(self.doors), figsize = (15, 5))
        for i in range(len(self.doors)):
            img = mpimg.imread(self.doors[i].image)
            axs[i].imshow(img)
            if self.doors[i].doorOpen:
                doorStatus = "Open"
            else:
                doorStatus = "Closed"
            axs[i].set_title("Door " + str(i + 1) + ": " + doorStatus)
        plt.show()

    def reveal_goat(self):
        for i in range(len(self.doors)):
            if i != self.contestant.doorChoice - 1 and not self.doors[i].prize:
                self.doors[i].openDoor()
                break

    def get_strategy(self):
        strategy = input("Choose strategy ['switch' or 'stay']: ")
        self.contestant.chooseStrategy(strategy)

    def reveal_all(self):
        for door in self.doors:
            door.openDoor()

    def result(self):
        chosenDoorLocation = self.contestant.doorChoice - 1
        chosenDoor = self.doors[chosenDoorLocation]

        if self.contestant.strategy == 'switch':
            for i in range(len(self.doors)):
                if i != chosenDoorLocation and not self.doors[i].doorOpen:
                    chosenDoor = self.doors[i]
                    break

        message = "Yay, you won!" if chosenDoor.prize else "Sorry, you lost."
        print(message)

    def simulate(n):
        switchRate = 0
        stayRate = 0

        for i in range(n):
            prize, choice = random.randint(1, 3), random.randint(1, 3)
            switch = random.choice([True, False])
    
            if switch:
                if choice != prize:
                    switchRate = switchRate + 1
            else:
                if choice == prize:
                    stayRate = stayRate + 1
    
        print("Switch Win Rate:", round(switchRate / n * 100, 2), "%")
        print("Stay Win Rate:", round(stayRate / n * 100, 2), "%")
    
    
    
