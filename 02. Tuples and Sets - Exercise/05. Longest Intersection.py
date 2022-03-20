n = int(input())
first_crossroad = set()
second_crossroad = set()
longest = set()
for _ in range(n):
    distance = input().split("-")
    one_side = [int(s) for s in distance[0].split(",")]
    two_side = [int(s) for s in distance[1].split(",")]
    for v in range(one_side[0], one_side[1]+1):
        first_crossroad.add(v)
    for s in range(two_side[0], two_side[1]+1):
        second_crossroad.add(s)
    x = first_crossroad.intersection(second_crossroad)
    if len(x) > len(longest):
        longest = first_crossroad.intersection(second_crossroad)
    first_crossroad = set()
    second_crossroad = set()

print(f"Longest intersection is [{', '.join([str(s) for s in longest])}] with length {len(longest)}")