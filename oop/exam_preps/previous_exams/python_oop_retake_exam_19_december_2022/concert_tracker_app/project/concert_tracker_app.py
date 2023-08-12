from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
	VALID_MUSICIAN_TYPES = {
		"Guitarist": Guitarist,
		"Drummer": Drummer,
		"Singer": Singer
	}

	def __init__(self):
		self.bands: List[Band] = []
		self.musicians: List[Musician] = []
		self.concerts: List[Concert] = []

	def create_musician(self, musician_type: str, name: str, age: int):
		if musician_type not in self.VALID_MUSICIAN_TYPES:
			raise ValueError("Invalid musician type!")

		musician = self.validate_by_name(name, self.musicians)

		if musician:
			raise Exception(f"{name} is already a musician!")

		self.musicians.append(self.VALID_MUSICIAN_TYPES[musician_type](name, age))

		return f"{name} is now a {musician_type}."

	def create_band(self, name: str):
		band = self.validate_by_name(name, self.bands)

		if band:
			raise Exception(f"{name} band is already created!")

		self.bands.append(Band(name))

		return f"{name} was created."

	def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
		concert_to_check = self.validate_concert(place, self.concerts)

		if concert_to_check:
			raise Exception(f"{place} is already registered for {concert_to_check.genre} concert!")

		concert = Concert(genre, audience, ticket_price, expenses, place)
		self.concerts.append(concert)

		return f"{concert.genre} concert in {concert.place} was added."

	def add_musician_to_band(self, musician_name: str, band_name: str):
		musician = self.validate_by_name(musician_name, self.musicians)
		band = self.validate_by_name(band_name, self.bands)

		if not musician:
			raise Exception(f"{musician_name} isn't a musician!")

		if not band:
			raise Exception(f"{band_name} isn't a band!")

		band.members.append(musician)

		return f"{musician_name} was added to {band_name}."

	def remove_musician_from_band(self, musician_name: str, band_name: str):
		band = self.validate_by_name(band_name, self.bands)

		if not band:
			raise Exception(f"{band_name} isn't a band!")

		musician = self.validate_by_name(musician_name, band.members)

		if not musician:
			raise Exception(f"{musician_name} isn't a member of {band_name}!")

		band.members.remove(musician)

		return f"{musician_name} was removed from {band_name}."

	def start_concert(self, concert_place: str, band_name: str):
		concert = self.validate_concert(concert_place, self.concerts)
		band = self.validate_by_name(band_name, self.bands)

		singers = [s for s in band.members if s.__class__.__name__ == "Singer"]
		drummers = [d for d in band.members if d.__class__.__name__ == "Drummer"]
		guitarists = [g for g in band.members if g.__class__.__name__ == "Guitarist"]

		if not singers or not drummers or not guitarists:
			raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

		play_concert = False

		if concert.genre == "Rock":
			drummer = [d for d in drummers if "play the drums with drumsticks" in d.skills]
			singer = [s for s in singers if "sing high pitch notes" in s.skills]
			guitarist = [g for g in guitarists if "play rock" in g.skills]

			if drummer and singer and guitarist:
				play_concert = True

		if concert.genre == "Metal":
			drummer = [d for d in drummers if "play the drums with drumsticks" in d.skills]
			singer = [s for s in singers if "sing low pitch notes" in s.skills]
			guitarist = [g for g in guitarists if "play metal" in g.skills]

			if drummer and singer and guitarist:
				play_concert = True

		if concert.genre == "Jazz":
			drummer = [d for d in drummers if "play the drums with drum brushes" in d.skills]
			singer = [s for s in singers if "sing low pitch notes" in s.skills and "sing high pitch notes" in s.skills]
			guitarist = [g for g in guitarists if "play jazz" in g.skills]

			if drummer and singer and guitarist:
				play_concert = True

		if not play_concert:
			raise Exception(f"The {band_name} band is not ready to play at the concert!")

		profit = concert.audience * concert.ticket_price - concert.expenses

		return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

	def validate_by_name(self, name: str, list_of_obj: list):
		for obj in list_of_obj:
			if obj.name == name:
				return obj

	def validate_concert(self, place: str, concerts: list):
		for c in concerts:
			if c.place == place:
				return c


musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
	print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
	print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
