from collections import deque
food = int(input())

orders = deque([int(s) for s in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()
    if food > order:
        food -= order
    else:
        orders.insert(0, order)
        print(f"Orders left: {' '.join([str(s) for s in orders])}")
        quit()
print("Orders complete")

