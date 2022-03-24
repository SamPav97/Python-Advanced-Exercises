command = input()
nums = [int(i) for i in input().split()]

if command == "Odd":
    odd = sum([i for i in nums if i % 2 != 0]) * len(nums)
    print(odd)
else:
    even = sum([i for i in nums if i % 2 == 0]) * len(nums)
    print(even)


