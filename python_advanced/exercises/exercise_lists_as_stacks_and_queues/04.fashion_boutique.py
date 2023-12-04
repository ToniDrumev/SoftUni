from collections import deque

box_with_clothes = deque(int(x) for x in input().split())
rack_size = int(input())
rack_count = 1
current_rack_size = 0

while box_with_clothes:
    current_cloth = box_with_clothes.pop()

    if current_rack_size + current_cloth <= rack_size:
        current_rack_size += current_cloth
    else:
        rack_count += 1
        current_rack_size = current_cloth

print(rack_count)
