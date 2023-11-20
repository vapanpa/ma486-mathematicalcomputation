import numpy as np
import matplotlib.pyplot as plt

from Server import Server
from Customer import Customer
from Event_List import Event_List
from Queue import Queue

def customerArrival(arrivalRate, maxTime):
    np.random.seed(1000)
    timing = 0
    customerID = 1
    customerList = Event_List()

    while timing <= maxTime:
        arrival = timing + np.random.exponential(arrivalRate)
        if arrival > maxTime:
            break
        customerList.addEvent(arrival, Customer(arrival, customerID), "Arrival")
        customerID = customerID + 1
        timing = arrival

    return customerList


# CITATIONS:
# Jake LaPorte. "MA486_Lsn28_1." Youtube, 11 Dec. 2020, www.youtube.com/watch?v=QQDkKN79zAg
# Jake LaPorte. "MA486_Lsn28_2." Youtube, 11 Dec. 2020, www.youtube.com/watch?v=VR9PaJ6_u6I


def availability(serverList):
    for i, server in enumerate(serverList):
        if not server.occupied():
            return [True, i]
    return [False]

def customerServer(serverList, customer):
    for server in serverList:
        if customer.number == server.customerNumber:
            return server

def simulate(filename, serverAmount, serverRates):
    queue_lengths = []  # To track queue length over time
    server_occupancy = {i: [] for i in range(serverAmount)}  # Track each server's occupancy
    wait_times = []  # Customer wait times

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
                    wait_times.append(0)  # No waiting time
                else:
                    customerQueue.enqueue(customer)
                    wait_times.append(eventTime - customer.getTime())  # Record waiting time
            elif event == "Departure":
                server = customerServer(serverList, customer)
                if server:
                    server.unOccupied()
                    if not customerQueue.isEmpty():
                        nextCustomer = customerQueue.dequeue()
                        endTime = server.serve(nextCustomer, eventTime)
                        customerEvent.addEvent(endTime, nextCustomer, "Departure")

            queue_lengths.append(len(customerQueue))
            for i, server in enumerate(serverList):
                server_occupancy[i].append(server.occupied())

            # Printing to file
            print(customerEvent, file=outfile)
            for item in serverList:
                print(item, file=outfile)
            print("=============== Customer Line ===============\n", file=outfile)
            print(customerQueue, file=outfile)
            if eventTime >= 100:
                break

    return queue_lengths, server_occupancy, wait_times


serverAmount = int(input("Server Amount: "))
serverRates = [float(input(f"Server {i+1} work rate: ")) for i in range(serverAmount)]

# simulate("results", serverAmount, serverRates)



def plot_simulation_data(queue_lengths, server_occupancy, wait_times):
    # Plot Customer Queue Length Over Time and save it as a PNG file
    plt.figure(figsize=(10, 6))
    plt.plot(queue_lengths, color='green')
    plt.xlabel('Event ID')
    plt.ylabel('Queue Length')
    plt.title('Customer Queue Length Over Time')
    plt.savefig('queue_lengths.png')
    plt.close()

    # Plot Server Occupancy Over Time and save it as a PNG file
    plt.figure(figsize=(10, 6))
    for server_id, occupancy in server_occupancy.items():
        plt.plot(occupancy, label=f'Server {server_id + 1}')
    plt.xlabel('Event ID')
    plt.ylabel('Server Occupancy (1 for busy, 0 for free)')
    plt.title('Server Occupancy Over Time')
    plt.legend()
    plt.savefig('server_occupancy.png')
    plt.close()

    # Plot Customer Wait Times and save it as a PNG file
    plt.figure(figsize=(10, 6))
    plt.hist(wait_times, bins=20, color='blue', edgecolor='black')
    plt.xlabel('Wait Time')
    plt.ylabel('Number of Customers')
    plt.title('Histogram of Customer Wait Times')
    plt.savefig('wait_times.png')
    plt.close()

# Call the function with the collected data
queue_lengths, server_occupancy, wait_times = simulate("results", serverAmount, serverRates)
plot_simulation_data(queue_lengths, server_occupancy, wait_times)

