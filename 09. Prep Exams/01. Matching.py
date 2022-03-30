from collections import deque

males = [int(i) for i in input().split()]
females = [int(i) for i in input().split()]
new_males = deque()
new_females = deque()
for ind in range(len(males)):
    if males[ind] != 0 and males[ind] % 25 == 0:
        males[ind] = 0
        males[ind+1] = 0
    if males[ind] > 0:
        new_males.append(males[ind])
for ind in range(len(females)):
    if females[ind] != 0 and females[ind] % 25 == 0:
        females[ind] = 0
        females[ind+1] = 0
    if females[ind] > 0:
        new_females.append(females[ind])
matches = 0
while True:
    if not new_females:
        break
    if not new_males:
        break
    male = new_males[-1]
    female = new_females[0]
    if male <= 0:
        new_males.pop()
        continue
    if female <= 0:
        new_females.popleft()
        continue

    if female == male:
        matches += 1
        new_males.pop()
        new_females.popleft()
    else:
        new_females.popleft()
        new_males.append(new_males.pop()-2)

print(f"Matches: {matches}")
if new_males:
    print(f"Males left: {', '.join(reversed([str(i) for i in new_males]))}")
else:
    print(f"Males left: none")

if new_females:
    print(f"Females left: {', '.join([str(i) for i in new_females])}")
else:
    print(f"Females left: none")
