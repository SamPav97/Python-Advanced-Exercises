from collections import deque

choc = deque([int(s) for s in input().split(", ")])
milk = deque([int(s) for s in input().split(", ")])
shakes = 0
while choc:
    if shakes == 5:
        break
    if len(milk) <= 0:
        break
    c = choc[-1]
    m = milk[0]

    if c == m:
        shakes += 1
        choc.pop()
        milk.popleft()
    elif c <= 0:
        choc.pop()
    elif m <= 0:
        milk.popleft()
    else:
        choc[-1] -= 5
        milk.append(milk.popleft())

if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")

else:
    print("Not enough milkshakes.")

if len(choc) > 0:
    print(f"Chocolate: {', '.join([str(i) for i in choc])}")
else:
    print("Chocolate: empty")
if len(milk) > 0:
    print(f"Milk: {', '.join([str(i) for i in milk])}")
else:
    print("Milk: empty")
