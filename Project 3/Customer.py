import numpy as np
import matplotlib.pyplot as plt


class Customer:
    def __init__(self, arrivalTime, number):
        self.Atime = arrivalTime
        self.number = number
        self.Dtime = -1


    def __repr__(self):
        return f"Customer({self.time:.3f})"

    def __str__(self):
        return f"{self.number}:{self.Atime:.3f},{self.Dtime:.3f}"

    def getTime(self):
        return self.Atime

    def __eq__(self, other):
        if type(other) != Customer:
            return False
        return self.number == other.number

