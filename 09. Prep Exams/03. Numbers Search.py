def numbers_searching(*args):
    args = sorted(args)
    maximum = max(args)
    minimum = min(args)
    all_nums = [i for i in range(minimum, maximum+1)]
    repeating = []
    missing = []
    for ind in range(len(args)-1):
        if args[ind] == args[ind+1]:
            repeating.append(args[ind+1])
    for num in all_nums:
        if num not in args:
            missing.append(num)
    missing.append(repeating)
    return missing


print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))