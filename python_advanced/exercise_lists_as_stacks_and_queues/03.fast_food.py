from collections import deque

food_in_stock = int(input())
orders = deque([int(order) for order in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()

    if current_order <= food_in_stock:
        food_in_stock -= current_order
    else:
        print(f"Orders left: {current_order} {' '.join([str(x)for x in orders])}")
        break

else:
    print("Orders complete")