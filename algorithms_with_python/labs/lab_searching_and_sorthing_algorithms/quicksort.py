numbers	= [int(x) for x in input(). split()]


def quicksort(nums, start, end):
	if start >= end:
		return

	pivot, left, right = start, start + 1, end
	while left <= right:
		if nums[left] > nums[pivot] > nums[right]:
			nums[left], nums[right] = nums[right], nums[left]

		if nums[left] <= nums[pivot]:
			left += 1

		if nums[right] >= nums[pivot]:
			right -= 1

	nums[pivot], nums[right] = nums[right], nums[pivot]

	quicksort(nums, start, right - 1)
	quicksort(nums, right + 1, end)

	return nums


result = quicksort(numbers, 0, len(numbers) - 1)
print(*result, sep=" ")
