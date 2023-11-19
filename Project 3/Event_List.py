import numpy as np
import matplotlib.pyplot as plt


class Event_List:
    def __init__(self):
        self.events = []

    def addEvent(self, time, entity, event):
        self.events.append((time, entity, event))
        self.events.sort(key=lambda x: x[0])

    def next(self):
        if self.events:
            return self.events.pop(0)
        return None

    def __str__(self):
        eventStream = "Time\tCustomer\tEvent\n"
        for index, (time, entity, event) in enumerate(self.events):
            eventStream = eventStream + f"{index}: {time:.3f}\t{entity}\t{event}\n"
        return eventStream

    def __len__(self):
        return len(self.events)