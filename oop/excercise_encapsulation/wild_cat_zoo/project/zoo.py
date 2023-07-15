from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
	def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
		self.name = name
		self.__budget = budget
		self.__animal_capacity = animal_capacity
		self.__workers_capacity = workers_capacity
		self.animals: List[Animal] = []
		self.workers: List[Worker] = []

	def add_animal(self, animal: Animal, price: int) -> str:
		if self.__animal_capacity == len(self.animals):
			return "Not enough space for animal"

		if price > self.__budget:
			return "Not enough budget"

		self.animals.append(animal)
		self.__budget -= price

		return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

	def hire_worker(self, worker: Worker) -> str:
		if self.__workers_capacity == len(self.workers):
			return "Not enough space for worker"

		self.workers.append(worker)

		return f"{worker.name} the {worker.__class__.__name__} hired successfully"

	def fire_worker(self, worker_name: str) -> str:
		workers = [w for w in self.workers if w.name == worker_name]

		if not workers:
			return f"There is no {worker_name} in the zoo"

		self.workers.remove(workers[0])

		return f"{worker_name} fired successfully"

	def pay_workers(self) -> str:
		salaries = sum([w.salary for w in self.workers])

		if salaries > self.__budget:
			return "You have no budget to pay your workers. They are unhappy"

		self.__budget -= salaries

		return f"You payed your workers. They are happy. Budget left: {self.__budget}"

	def tend_animals(self) -> str:
		sum_for_tending = sum([a.money_for_care for a in self.animals])

		if sum_for_tending > self.__budget:
			return "You have no budget to tend the animals. They are unhappy."

		self.__budget -= sum_for_tending

		return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

	def profit(self, amount: int) -> None:
		self.__budget += amount

	def animals_status(self) -> str:
		result = f"You have {len(self.animals)} animals\n"

		lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
		tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
		cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

		result += f"----- {len(lions)} Lions:\n" + "\n".join([str(l) for l in lions]) + "\n"
		result += f"----- {len(tigers)} Tigers:\n" + "\n".join([str(t) for t in tigers]) + "\n"
		result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join([str(c) for c in cheetahs])

		return result

	def workers_status(self) -> str:
		result = f"You have {len(self.workers)} workers\n"

		keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
		caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
		vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

		result += f"----- {len(keepers)} Keepers:\n" + "\n".join([str(k) for k in keepers]) + "\n"
		result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join([str(c) for c in caretakers]) + "\n"
		result += f"----- {len(vets)} Vets:\n" + "\n".join([str(v) for v in vets])

		return result
