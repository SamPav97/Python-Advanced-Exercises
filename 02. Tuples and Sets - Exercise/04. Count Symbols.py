text = input()

occurances = {}

for l in text:
    if l not in occurances.keys():
        occurances[l] = 0
    occurances[l] += 1

ordered = {k: v for k, v in sorted(occurances.items(), key= lambda x: x)}

for k,v in ordered.items():
    print(f"{k}: {v} time/s")