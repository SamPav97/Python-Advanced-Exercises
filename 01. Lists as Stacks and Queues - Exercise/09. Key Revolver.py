from collections import deque
bull_price = int(input())
mag = int(input())
bullets = deque([int(s) for s in input().split()])
given_bullets = len(bullets)
locks = deque([int(s) for s in input().split()])
value_of_whiskey = int(input())
count = 0
while locks:
    if bullets:
        bullet = bullets.pop()
    else:
        break
    lock = locks.popleft()
    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)
    count += 1
    if count % mag == 0 and bullets:
        print("Reloading!")


costs = (given_bullets - len(bullets)) * bull_price

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_of_whiskey-costs}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
