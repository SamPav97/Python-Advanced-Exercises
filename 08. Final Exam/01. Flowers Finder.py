from collections import deque

lst = deque()
lst.append(set(list("rose")))
lst.append(set(list("tulip")))
lst.append(set(list("lotus")))
lst.append(set(list("daffodil")))

vowels = deque(input().split())
const = deque(input().split())

while True:
    if not vowels:
        print("Cannot find any word!")
        break
    if not const:
        print("Cannot find any word!")
        break

    vowl = vowels.popleft()
    con = const.pop()

    for _ in range(len(lst)):
        check = lst.popleft()
        while vowl in check:
            check.remove(vowl)
        while con in check:
            check.remove(con)
        lst.append(check)

    flower = None
    for ind in range(len(lst)):
        if not lst[ind]:
            if ind == 0:
                flower = "rose"
            if ind == 1:
                flower = "tulip"
            if ind == 2:
                flower = "lotus"
            if ind == 3:
                flower = "daffodil"

    if flower:
        print(f"Word found: {flower}")
        break

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if const:
    print(f"Consonants left: {' '.join(const)}")

