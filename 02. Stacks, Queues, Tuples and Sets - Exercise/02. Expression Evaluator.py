from collections import deque

stuff = deque(input().split())
temp = deque()

for element in stuff:

    if element in "+-/*":
        while len(temp) > 1:
            first = int(temp.popleft())
            second = int(temp.popleft())
            result = 0
            if element == "+":
                result = first + second
            elif element == "-":
                result = first - second
            elif element == "*":
                result = first * second
            elif element == "/":
                result = first // second

            temp.appendleft(str(result))
    else:
        temp.append(element)
print(*temp)