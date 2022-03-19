from collections import deque

nums_stack = deque(input().split())

while nums_stack:
    print(nums_stack.pop(), end=" ")