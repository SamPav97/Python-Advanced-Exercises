from collections import deque
def fill_the_box(*args):
    things = deque(args)
    size = things.popleft() * things.popleft() * things.popleft()
    while things:
        thing = things.popleft()
        if thing == "Finish":
            return f"There is free space in the box. You could put {size} more cubes."
        if thing <= size:
            size -= thing
        else:
            thing -= size
            things.appendleft(thing)
            things.pop()
            return f"No more free space! You have {sum(things)} more cubes."



print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))