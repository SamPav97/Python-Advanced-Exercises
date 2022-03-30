from collections import deque


def list_manipulator(lst, command, location, *args):
    lst = deque(lst)
    if command == "add":
        if location == "beginning":
            lst.extendleft(reversed(args))
            return list(lst)
        elif location == "end":
            lst.extend(args)
            return list(lst)
    elif command == "remove":
        if location == "beginning":
            if args:
                for _ in range(args[0]):
                    lst.popleft()
                return list(lst)
            else:
                lst.popleft()
                return list(lst)
        elif location == "end":
            if args:
                for _ in range(args[0]):
                    lst.pop()
                return list(lst)
            else:
                lst.pop()
                return list(lst)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
