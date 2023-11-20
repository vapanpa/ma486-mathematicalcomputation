import numpy as np
import matplotlib.pyplot as plt


class Server:
    def __init__(self, server_number, service_rate):
        self.busy = False
        self.number = server_number
        self.rate = service_rate
        self.customer = None
        self.customerNumber = None

    def __repr__(self):
        return f"Server {self.number}: Customer=>{self.customer}; Busy=>{self.busy}; ServiceRate=>{1/self.rate:.3f}"

    def occupied(self):
        return self.busy

    def unOccupied(self):
        self.busy = False
        self.customer = None
        self.customerNumber = None

    def beginService(self):

        self.busy = True

    def serve(self, cust, arrivalTime):
        self.beginService()
        self.customer = cust
        self.customerNumber = cust.number
        np.random.seed(220)
        timeServe = np.random.exponential(self.rate,1)[0]
        cust.departure_time = cust.arrival_time + timeServe
        return cust.departure_time

    def __lt__(self, other):
        return self.rate < other.rate

    def __gt__(self, other):
        return self.rate > other.rate


# CITATIONS: