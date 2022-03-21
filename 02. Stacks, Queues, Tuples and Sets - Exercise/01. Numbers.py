first = set([int(s) for s in input().split()])
second = set([int(s) for s in input().split()])
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for thing in command[2:]:
                first.add(int(thing))
        else:
            for thing in command[2:]:
                second.add(int(thing))
    elif command[0] == "Remove":
        if command[1] == "First":
            first = first.difference([int(x) for x in command[2:]])
        else:
            second = second.difference([int(x) for x in command[2:]])
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")

