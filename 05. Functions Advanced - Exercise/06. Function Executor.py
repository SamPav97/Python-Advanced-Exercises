def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    lst = []
    for funct, argu in args:
        lst.append(funct(*argu))
    return lst


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

