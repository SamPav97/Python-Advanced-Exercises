from collections import deque

clothes_stack = deque([int(s) for s in input().split()])
capacity_rack = int(input())
hang = 0
rafts = 0
while clothes_stack:
    while hang < capacity_rack:
        if len(clothes_stack) == 0:
            break
        clothing = clothes_stack.pop()
        hang += clothing
    rafts += 1
    if hang > capacity_rack:
        clothes_stack.append(clothing)
    hang = 0
print(rafts)


