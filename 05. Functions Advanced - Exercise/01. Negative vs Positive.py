nums = [int(i) for i in input().split()]

pos = sum([i for i in nums if i > 0])
neg = sum([i for i in nums if i < 0])

print(neg)
print(pos)

if abs(neg) > pos:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")