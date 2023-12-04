import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str):
	Pet.objects.create(
		name=name,
		species=species
	)

	return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
	Artifact.objects.create(
		name=name,
		origin=origin,
		age=age,
		description=description,
		is_magical=is_magical,
	)

	return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
	Artifact.objects.all().delete()


def show_all_locations():
	locations_model = Location.objects.all().order_by('-id')

	return '\n'.join(str(lm) for lm in locations_model)


def new_capital():
	Location.objects.filter(id=1).update(is_capital=True)


def get_capitals():
	return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
	Location.objects.first().delete()


def apply_discount():
	cars = Car.objects.all()

	for c in cars:
		percentage_to_decrease = sum(int(x) for x in str(c.year)) / 100
		c.price_with_discount = float(c.price) * (1 - percentage_to_decrease)
		c.save()


def get_recent_cars():
	return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
	Car.objects.last().delete()


def show_unfinished_tasks():
	unfinished_tasks = Task.objects.filter(is_finished=False)
	result = []

	for t in unfinished_tasks:
		result.append(f"Task - {t.title} needs to be done until {t.due_date}!")

	return "\n".join(result)


def complete_odd_tasks():
	for t in Task.objects.all():
		if t.id % 2 != 0:
			t.is_finished = True
			t.save()


def encode_and_replace(text: str, task_title: str):
	tasks = Task.objects.filter(title=task_title)

	for task in tasks:
		task.description = ''.join(chr(ord(c) - 3) for c in text)
		task.save()


def get_deluxe_rooms():
	deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
	result = []

	for room in deluxe_rooms:
		if room.id % 2 == 0:
			result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

	return '\n'.join(result)


def increase_room_capacity():
	rooms = HotelRoom.objects.all()

	previous_room_capacity = None

	for r in rooms:
		if not r.is_reserved:
			continue

		if previous_room_capacity:
			r.capacity += previous_room_capacity
		else:
			r.capacity += r.id

		previous_room_capacity = r.capacity

		r.save()


def reserve_first_room():
	first_room = HotelRoom.objects.first()
	first_room.is_reserved = True
	first_room.save()


def delete_last_room():
	last_room = HotelRoom.objects.last()

	if last_room.is_reserved:
		last_room.delete()
