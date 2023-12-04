from typing import Dict


class dictionary_iter:
	def __init__(self, dictionary: Dict) -> None:
		self.dictionary = dictionary
		self.list_dict_items = list(self.dictionary.items())
		self.current_index = 0

	def __iter__(self):
		return self

	def __next__(self):
		i = self.current_index

		if i < len(self.list_dict_items):
			self.current_index += 1

			return self.list_dict_items[i]

		else:
			raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
	print(x)

result = dictionary_iter({"name": "Peter",
"age": 24})
for x in result:
	print(x)