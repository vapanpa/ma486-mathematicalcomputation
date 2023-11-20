import numpy as np
import matplotlib.pyplot as plt


class Customer:
    def __init__(self, arrivalTime, number):
        self.arrival_time = arrivalTime
        self.number = number
        self.departure_time = -1

    def __repr__(self):
        return "Customer({:.3f})".format(self.arrival_time)

    def __str__(self):
        return "{}:{:.3f},{:.3f}".format(self.number, self.arrival_time, self.departure_time)

    def getTime(self):
        return self.arrival_time

# CITATION:
    # Difference Between “__Eq__” VS “is” VS “==” in Python. www.tutorialspoint.com/difference-between-eq-vs-is-vs-in-python#:~:
    # text=The%20__eq__%20method%20in%20Python%20is%20used%20to,value(True%20or%20False).

    def __eq__(self, other):
        if type(other) != Customer:
            return False
        return self.number == other.number

