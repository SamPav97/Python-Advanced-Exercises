from collections import deque

bomb_effects = deque([int(i) for i in input().split(", ")])
casings = deque([int(i) for i in input().split(", ")])
bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
while True:
    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break
    if not bomb_effects:
        print("You don't have enough materials to fill the bomb pouch.")
        break
    if not casings:
        print("You don't have enough materials to fill the bomb pouch.")
        break

    effect = bomb_effects[0]
    casing = casings[-1]

    if effect + casing == 40:
        bombs["Datura Bombs"] += 1
        bomb_effects.popleft()
        casings.pop()
    elif effect + casing == 60:
        bombs["Cherry Bombs"] += 1
        bomb_effects.popleft()
        casings.pop()
    elif effect + casing == 120:
        bombs["Smoke Decoy Bombs"] += 1
        bomb_effects.popleft()
        casings.pop()
    else:
        casings.append((casings.pop()-5))
        continue


if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(i) for i in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(i) for i in casings])}")
else:
    print("Bomb Casings: empty")

sortednames = {k: v for k, v in sorted(bombs.items(), key=lambda x: x[0])}

for k, v in sortednames.items():
    print(f"{k}: {v}")