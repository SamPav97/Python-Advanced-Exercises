from collections import deque

stack = []
n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))
    elif command[0] == "2" and len(stack) > 0:
        stack.pop()
    elif command[0] == "3" and len(stack) > 0:
        print(max(stack))
    elif command[0] == "4" and len(stack) > 0:
        print(min(stack))
    else:
        continue

print(", ".join(reversed([str(s) for s in stack])))