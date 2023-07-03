from typing import List, Dict

from project.user import User


class Library:
	def __init__(self):
		self.user_records: List[User] = []
		self.books_available: Dict[str: List[str]] = {}  # Dict{author1: [book1, book2, ...], ...}
		self.rented_books: Dict[
						   str: Dict[str: int]] = {}  # Dict{username1: {book1: days_to_ret, book2: days, ...}, ...}

	def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
		if book_name not in self.books_available[author]:
			for username, book in self.rented_books.items():
				if book_name in book:
					return f"The book \"{book_name}\" is already rented and will be available in " \
						   f"{self.rented_books[username][book_name]} days!"

		if user.username not in self.rented_books:
			self.rented_books[user.username] = {}

		user.books.append(book_name)
		self.books_available[author].remove(book_name)
		self.rented_books[user.username][book_name] = days_to_return

		return f"{book_name} successfully rented for the next {days_to_return} days!"

	def return_book(self, author: str, book_name: str, user: User) -> str:
		if book_name not in user.books:
			return f"{user.username} doesn't have this book in his/her records!"

		self.books_available[author].append(book_name)
		self.rented_books[user.username].pop(book_name)
		user.books.remove(book_name)
