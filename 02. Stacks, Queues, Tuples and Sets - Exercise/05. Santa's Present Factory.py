from collections import deque


def toy(plastic, wizard):
    if plastic * wizard == 150:
        toys.append("Doll")
        return 150
    elif plastic * wizard == 250:
        toys.append("Wooden train")
        return 250
    elif plastic * wizard == 300:
        toys.append("Teddy bear")
        return 300
    elif plastic * wizard == 400:
        toys.append("Bicycle")
        return 400
    elif plastic * wizard < 0:
        return plastic * wizard
    else:
        return plastic * wizard


materials = deque([int(s) for s in input().split()])
magic = deque([int(s) for s in input().split()])
toys = []
while True:
    if len(materials) == 0:
        break
    elif len(magic) == 0:
        break

    mater = materials[-1]
    mag = magic[0]
    if toy(mater, mag) in [400, 300, 250, 150]:
        materials.pop()
        magic.popleft()
    elif toy(mater, mag) < 0:
        mat = materials.pop()
        mag = magic.popleft()
        materials.append(mat+mag)
    elif toy(mater, mag) > 0:
        mag = magic.popleft()
        materials[-1] += 15
    else:
        if mater == 0:
            materials.pop()
        if mag == 0:
            magic.popleft()

if ("Doll" in toys and "Train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(reversed([str(i) for i in materials]))}")
if magic:
    print(f"Magic left: {', '.join(reversed([str(i) for i in magic]))}")

things = {}

for toy in toys:
    if toy not in things.keys():
        things[toy] = 0
    things[toy] += 1

ordered = {k: v for k, v in sorted(things.items(), key= lambda x: x)}

for k, v in ordered.items():
    print(f"{k}: {v}")