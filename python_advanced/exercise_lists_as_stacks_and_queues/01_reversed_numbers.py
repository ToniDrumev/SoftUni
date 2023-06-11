"""Simple reversed numbers exercise."""

from collections import deque

nums = deque(input().split())
reversed_nums = deque()

while nums:
    reversed_nums.append(nums.pop())

print(" ".join(reversed_nums))