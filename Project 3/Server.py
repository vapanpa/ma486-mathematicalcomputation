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


    def isBusy(self):
        return self.busy

    def freeUp(self):
        self.busy = False
        self.customer = None
        self.customerNumber = None

    def makeBusy(self):

        self.busy = True

    def serve(self, cust, arrivalTime):
        self.makeBusy()
        self.customer = cust
        self.customerNumber = cust.number
        np.random.seed(220)
        timeServe = np.random.exponential(self.rate,1)[0]
        cust.Dtime = cust.Atime + timeServe
        return cust.Dtime

    def __lt__(self, other):
        return self.rate < other.rate

    def __gt__(self, other):
        return self.rate > other.rate


# CITATIONS: