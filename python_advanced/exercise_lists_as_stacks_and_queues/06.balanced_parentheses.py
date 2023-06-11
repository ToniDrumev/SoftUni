from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    current_char = parentheses.popleft()

    if current_char in "({[":
        open_parentheses.append(current_char)
    elif not open_parentheses:
        print("NO")
        break
    else:
        if open_parentheses.pop() + current_char not in "()[]{}":
            print("NO")
            break
else:
    print("YES")

