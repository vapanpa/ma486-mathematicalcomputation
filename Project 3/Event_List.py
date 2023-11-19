import numpy as np
import matplotlib.pyplot as plt


class Event_List:
    def __init__(self):
        self.time = []
        self.entity = []
        self.event = []
        self.previousTime = 0

    def __str__(self):
        result = str(self.previousTime) + "\n"
        result = result + "# : Time  \t     Customer \t\t       Event " +"\n"
        for i in range(len(self.time)):
            result = result + f"{i:<2.0f}"+":"+" {:<8.3f}\t {:<8} \t{:>10}".format(float(self.time[i]),str(self.entity[i]),self.event[i])+"\n"
        return result

    def __repr__(self):
        result = ""
        for i in range(len(self.time)):
            result = result + f"{i:<2.0f}"+":"+" {:<8.3f}\t {:<8} \t{:>10}".format(float(self.time[i]),str(self.entity[i]),self.event[i])+"\n"
        return result

    def addEvent(self, time, entity, event):
        current = time
        self.time.append(time)
        self.time.sort()
        index = self.time.index(current)
        self.entity.insert(index, entity)
        self.event.insert(index, event)

    def next(self):
        time = self.time[0]
        entity = self.entity[0]
        event = self.event[0]
        self.previousTime = time
        del (self.time[0])
        del (self.entity[0])
        del (self.event[0])
        return time, entity, event

    def __len__(self):
        return len(self.event)