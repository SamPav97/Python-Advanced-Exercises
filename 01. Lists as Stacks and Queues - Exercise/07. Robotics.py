from collections import deque

def convert_str_to_seconds(str_time):
    time_separated = str_time.split(":")
    hours_to_seconds = int(time_separated[0]) * 60 * 60
    minutes_to_secodns = int(time_separated[1]) * 60
    seconds = int(time_separated[2])
    total_time_in_secs = hours_to_seconds+minutes_to_secodns+seconds
    return total_time_in_secs


def convert_seconds_to_string_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)




robots_data = input().split(";")
process_time_by_robot = {}
busy_time_by_robot = {}
for robot_data in robots_data:
    name, process_time = robot_data.split("-")
    process_time_by_robot[name] = int(process_time)
    busy_time_by_robot[name] = -1

time = convert_str_to_seconds(input())

items = deque()
while True:
    command = input()
    if command == "End":
        break
    items.append(command)

while items:
    time += 1
    item = items.popleft()
    for name, busy_until in busy_time_by_robot.items():
        if time >= busy_until:
            print(f"{name} - {item} [{convert_seconds_to_string_time(time)}]")
            busy_time_by_robot[name] = time + process_time_by_robot[name]
            break
    else:
        items.append(item)

