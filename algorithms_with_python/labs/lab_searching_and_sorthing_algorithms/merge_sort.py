numbers	= [int(x) for x in input(). split()]


def merge_arrays(left, right):
	pass


def merge_sort(nums):
	if len(nums) == 1:
		return nums

	middle = len(nums) // 2

	left = nums[:middle]
	right = nums[middle:]

	return merge_arrays(merge_sort(left), merge_sort(right))
	
	