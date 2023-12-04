from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
	VALID_LOAN_TYPES = {
		"StudentLoan": StudentLoan,
		"MortgageLoan": MortgageLoan
	}

	VALID_CLIENT_TYPES = {
		"Student": Student,
		"Adult": Adult
	}

	VALID_LOANS_BY_CLIENT = {
		"Student": "StudentLoan",
		"Adult": "MortgageLoan"
	}

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.loans = []
		self.clients = []

	def add_loan(self, loan_type: str) -> str:
		if loan_type not in self.VALID_LOAN_TYPES:
			raise Exception("Invalid loan type!")

		self.loans.append(self.VALID_LOAN_TYPES[loan_type]())

		return f"{loan_type} was successfully added."

	def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
		if client_type not in self.VALID_CLIENT_TYPES:
			raise Exception("Invalid client type!")

		if len(self.clients) == self.capacity:
			return "Not enough bank capacity."

		self.clients.append(self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income))

		return f"{client_type} was successfully added."

	def grant_loan(self, loan_type: str, client_id: str) -> str:
		client = self.validate_client_by_id(client_id, self.clients)

		if self.VALID_LOANS_BY_CLIENT[client.__class__.__name__] != loan_type:
			raise Exception("Inappropriate loan type!")

		for loan in self.loans:
			if loan.__class__.__name__ == loan_type:
				self.loans.remove(loan)
				client.loans.append(loan)
				break

		return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

	def remove_client(self, client_id: str):
		client = self.validate_client_by_id(client_id, self.clients)

		if not client:
			raise Exception("No such client!")

		if client.loans:
			raise Exception("The client has loans! Removal is impossible!")

		for c in self.clients:
			if c.client_id == client.client_id:
				self.clients.remove(c)
				break

		return f"Successfully removed {client.name} with ID {client_id}."

	def increase_loan_interest(self, loan_type: str):
		counter = 0

		for loan in self.loans:
			if loan.__class__.__name__ == loan_type:
				loan.increase_interest_rate()
				counter += 1

		return f"Successfully changed {counter} loans."

	def increase_clients_interest(self, min_rate: float):
		counter = 0

		for cl in self.clients:
			if cl.interest < min_rate:
				cl.increase_clients_interest()
				counter += 1

		return f"Number of clients affected: {counter}."

	def get_statistics(self):
		if self.clients:
			average_client_rate = sum([c.interest for c in self.clients]) / len(self.clients)
		else:
			average_client_rate = 0

		loans_count_granted_to_clients = 0
		granted_sum = 0

		for client in self.clients:
			loans_count_granted_to_clients += len(client.loans)

			for loan in client.loans:
				granted_sum += loan.amount

		result = f"Active Clients: {len(self.clients)}\n" + \
				 f"Total Income: {sum([cl.income for cl in self.clients]):.2f}\n" + \
				 f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" + \
				 f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}\n" + \
				 f"Average Client Interest Rate: {average_client_rate:.2f}"

		return result

	def validate_client_by_id(self, client_id: str, list_of_clients: list):
		for client in list_of_clients:
			if client.client_id == client_id:
				return client

