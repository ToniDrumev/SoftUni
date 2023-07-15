from typing import List
from math import ceil


class PhotoAlbum:
	PAGE_MAX_SIZE = 4

	def __init__(self, pages: int) -> None:
		self.pages = pages
		self.photos: List[List[str]] = [[] for _ in range(self.pages)]
		self.page_number = 0

	@classmethod
	def from_photos_count(cls, photos_count: int):
		cur_pages = ceil(photos_count / PhotoAlbum.PAGE_MAX_SIZE)
		return cls(cur_pages)

	def add_photo(self, label: str) -> str:
		if len(self.photos[self.page_number]) == self.PAGE_MAX_SIZE:
			self.page_number += 1

		if self.page_number == self.pages:
			return "No more free slots"

		self.photos[self.page_number].append(label)

		return f"{label} photo added successfully on page " \
			   f"{self.page_number + 1} slot " \
			   f"{len(self.photos[self.page_number])}"

	def display(self) -> str:
		result = ["-" * 11]
		for p in self.photos:
			result.append(" ".join(["[]" for _ in p]))
			result.append("-" * 11)

		return "\n".join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())


