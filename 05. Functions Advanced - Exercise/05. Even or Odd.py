def even_odd(*args):
    command = args[-1]
    nums = [int(i) for i in args[:-1]]
    if command == "odd":
        odd = [i for i in nums if i % 2 != 0]
        return odd
    else:
        even = [i for i in nums if i % 2 == 0]
        return even


print(even_odd(1, 2, 3, 4, 5, 6, "even"))