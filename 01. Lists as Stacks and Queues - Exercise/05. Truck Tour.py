from collections import deque

num_petr_stations = int(input())
stats_stack = deque()
for _ in range(num_petr_stations):
    pump_data = [int(x) for x in input().split()]
    stats_stack.append(pump_data)

for attempt in range(num_petr_stations):
    tank = 0
    full_dist = 0
    failed = False
    for fuel, distance in stats_stack:
        tank += fuel
        full_dist += distance
        if full_dist > tank:
            failed = True
            break
    if failed:
        stats_stack.append(stats_stack.popleft())
    else:
        print(attempt)
        break



# success = True
# total_gas = 0
# for attempt in range(num_petr_stations):
#     station = stats_stack.popleft().split()
#     gas = int(station[0])
#     distance = int(station[1])
#     for x in station:
#         total_gas += int(gas)
#         if int(distance) > total_gas:
#             success = False
#
#             break
#     if success is True:
#         print(attempt)





# count = 0
# while True:
#     count += 1
#     comparison = stats_stack.popleft().split()
#     if int(comparison[0]) < int(comparison[1]):
#         continue
#     else:
#         break
# print(count-1)

