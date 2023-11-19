import numpy as np
from Server import Server
from Customer import Customer
from Event_List import Event_List
from Queue import Queue

def customerArrival(arrivalRate, maxTime):
    np.random.seed(1000)
    timing = 0
    cust = 1
    customerList = Event_List()

    while timing <= maxTime:
        arrival = timing + np.random.exponential(arrivalRate)
        if arrival > maxTime:
            break
        customerList.addEvent(arrival, Customer(arrival, cust), "Arrival")
        cust = cust + 1
        timing = arrival

    return customerList


# CITATIONS:

def availability(serverList):
    for i, server in enumerate(serverList):
        if not server.isBusy():
            return [True, i]
    return [False]

def customerServer(serverList, customer):
    for server in serverList:
        if customer.number == server.customerNumber:
            return server

def simulate(filename, serverAmount, serverRates):
    with open(f"{filename}.txt", "w") as outfile:
        customerQueue = Queue()
        customerEvent = customerArrival(5, 100)
        serverList = [Server(x + 1, serverRates[x]) for x in range(serverAmount)]

        while len(customerEvent):
            eventTime, customer, event = customerEvent.next()

            if event == "Arrival":
                available = availability(sorted(serverList))
                if available[0]:
                    server = serverList[available[1]]
                    endTime = server.serve(customer, eventTime)
                    customerEvent.addEvent(endTime, customer, "Departure")
                else:
                    customerQueue.enqueue(customer)
            elif event == "Departure":
                server = customerServer(serverList, customer)
                if server:
                    server.freeUp()
                    if not customerQueue.isEmpty():
                        nextCustomer = customerQueue.dequeue()
                        endTime = server.serve(nextCustomer, eventTime)
                        customerEvent.addEvent(endTime, nextCustomer, "Departure")

            print(customerEvent, file = outfile)
            for x in serverList:
                print(x, file = outfile)
            print("=====Customer Line ===============\n", file = outfile)
            print(customerQueue, file = outfile)  # Print the queue state
            if eventTime >= 100:
                break

    print("--> results.txt")

serverAmount = int(input("Server Amount: "))
serverRates = [float(input(f"Server {i+1} work rate: ")) for i in range(serverAmount)]

simulate("results", serverAmount, serverRates)
