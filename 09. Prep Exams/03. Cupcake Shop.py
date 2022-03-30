from collections import deque


def stock_availability(stock, command, *args):
    stock = deque(stock)
    if command == "delivery":
        stock.extend(args)
    else:
        if args:
            if str(args[0]).isdigit():
                for box in range(int(args[0])):
                    stock.popleft()
            else:
                for el in args:
                    try:
                        while True:
                            stock.remove(el)
                    except ValueError:
                        pass

        else:
            stock.popleft()
    return list(stock)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
