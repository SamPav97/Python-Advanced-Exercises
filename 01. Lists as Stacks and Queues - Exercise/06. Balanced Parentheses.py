expression = input()
opening_brax = []
balanced = True

for ch in expression:
    if ch in "{[(":
        opening_brax.append(ch)
    elif not opening_brax:
        balanced = False
        break
    else:
        last_brax = opening_brax.pop()
        if f"{last_brax}{ch}" not in "(){}[]":
            balanced = False
            break

if balanced and not opening_brax:
    print("YES")
else:
    print("NO")