def reverse_array(nums, index):
	if index == len(nums):
		return

	reverse_array(nums, index + 1)
	print(nums[index], end=" ")


numbers = [n for n in input().split()]

reverse_array(numbers, 0)