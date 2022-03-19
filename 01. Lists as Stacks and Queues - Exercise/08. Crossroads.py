from collections import deque
green = int(input())
free_window = int(input())
temp_green = green
count = 0
cars = deque()
while True:

    command = input()
    if command == "END":
        break

    elif command == "green":
        temp_green = green

        while temp_green > 0 and cars:
            car = cars[0]

            if len(car) <= temp_green:
                temp_green -= len(car)
                cars.popleft()
                count += 1
            elif 0 < temp_green < len(car):
                if len(car) <= temp_green + free_window:
                    temp_green = 0
                    cars.popleft()
                    count += 1
                else:
                    print("A crash happened!")
                    hit_at = temp_green + free_window
                    print(f"{car} was hit at {car[hit_at]}.")
                    quit()

    else:
        cars.append(command)


print("Everyone is safe.")
print(f"{count} total cars passed the crossroads.")