from collections import deque

customers = deque(input().split(", "))
taxis = deque(input().split(", "))
total_time = 0

while True:
    if not customers:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
        break
    if not taxis:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(customers)}")
        break


    customer = int(customers[0])
    taxi = int(taxis[-1])

    if customer <= taxi:
        total_time += int(customers.popleft())
        taxis.pop()
    else:
        taxis.pop()