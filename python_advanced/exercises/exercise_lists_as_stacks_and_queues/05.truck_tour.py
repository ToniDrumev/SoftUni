from collections import deque

num_of_stations = int(input())
fuel_tank = 0
index = 0

station_args = deque([[int(x) for x in input().split()] for _ in range(num_of_stations)])

stations_copy = station_args.copy()

while stations_copy:
    current_station_args = stations_copy.popleft()

    fuel_tank += current_station_args[0]
    distance = current_station_args[1]

    if distance > fuel_tank:
        station_args.rotate(-1)
        stations_copy = station_args.copy()
        index += 1
        fuel_tank = 0
    else:
        fuel_tank -= distance

print(index)
