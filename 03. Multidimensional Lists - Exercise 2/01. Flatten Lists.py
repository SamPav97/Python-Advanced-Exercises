all = input().split("|")
final = []
while all:
    final.extend(all.pop().split())
print(*final)