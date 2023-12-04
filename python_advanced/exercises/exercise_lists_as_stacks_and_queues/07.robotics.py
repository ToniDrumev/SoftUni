from collections import deque
from datetime import datetime, timedelta

robots = {robot: [int(process_time), 0] for robot, process_time in [el.split("-") for el in input().split(";")]}

starting_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()
product = input()

while product != "End":
    products.append(product)
    product = input()

while products:
    starting_time += timedelta(seconds=1)

    free_robots = deque()

    for robot in robots:
        if robots[robot][1] != 0:
            robots[robot][1] -= 1

        if robots[robot][1] == 0:
            free_robots.append(robot)

    if free_robots:
        current_robot = free_robots.popleft()
        print(f"{current_robot} - {products.popleft()} [{starting_time.strftime('%H:%M:%S')}]")
        robots[current_robot][1] = robots[current_robot][0]
    else:
        products.append(products.popleft())
