first, second = [int(s) for s in input().split()]
set_1 = set()
set_2 = set()
for _ in range(first):
    set_1.add(input())
for _ in range(second):
    set_2.add(input())

x = set_1.intersection(set_2)

print(type(x))

for el in x:
    print(el)