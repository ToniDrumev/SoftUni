def even_parameters(func):
	def wrapper(*args, **kwargs):
		even_numbers = []

		for num in args:
			if type(num) != int or num % 2 != 0:
				return "Please use only even numbers!"

			even_numbers.append(num)

		return func(*even_numbers)

	return wrapper


@even_parameters
def multiply(*nums):
	result = 1

	for num in nums:
		result *= num

	return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
