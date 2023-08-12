def type_check(type_of_arg):
	def decorator(func):
		def wrapper(*args, **kwargs):
			if type(*args) != type_of_arg:
				return "Bad Type"

			return func(*args)

		return wrapper

	return decorator


@type_check(str)
def first_letter(word):
	return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
