import numpy as np
import matplotlib.pyplot as plt


class Queue:
    def __init__(self):
        self.customers = []

    def enqueue(self, customer):
        self.customers.append(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.customers.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.customers[0]

    def is_empty(self):
        return len(self.customers) == 0

    def __len__(self):
        return len(self.customers)

    def __str__(self):
        return f"Queue: {[customer.number for customer in self.customers]}"

    def __repr__(self):
        return str(self)
