from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

	def setUp(self) -> None:
		self.student = Student("Some name")

	def test_check_correct_initialize_method(self):

		self.assertEqual("Some name", self.student.name)
		self.assertEqual({}, self.student.courses)
		self.assertIsInstance(self.student.name, str)
		self.assertIsInstance(self.student.courses, dict)

	def test_check_if_course_name_in_course_keys_and_update_notes(self):
		self.student.courses["some course"] = []

		actual = self.student.enroll("some course", ['1', '2', '3'], "acn")

		self.assertEqual("Course already added. Notes have been updated.", actual)
		self.assertEqual(['1', '2', '3'], self.student.courses["some course"])

	def test_add_course_with_course_notes(self):
		result = self.student.enroll("some course", ["1", "2"], "Y")

		self.assertEqual(["1", "2"], self.student.courses["some course"])
		self.assertEqual("Course and course notes have been added.", result)

		result = self.student.enroll("other course", ["new", "notes"], "")

		self.assertEqual(["new", "notes"], self.student.courses["other course"])
		self.assertEqual("Course and course notes have been added.", result)

	def test_add_empty_course(self):
		result = self.student.enroll("some course", ["1", "2"], "new")

		self.assertEqual({"some course": []}, self.student.courses)
		self.assertEqual([], self.student.courses["some course"])
		self.assertEqual("Course has been added.", result)

		result = self.student.enroll("other course", ["1", "2"], "new")

		self.assertEqual({"some course": [], "other course": []}, self.student.courses)
		self.assertEqual([], self.student.courses["other course"])
		self.assertEqual("Course has been added.", result)

		result = self.student.enroll("other course", ["1", "2"], "new")

		self.assertEqual("Course already added. Notes have been updated.", result)

	def test_add_notes_if_course_name_in_courses(self):
		self.student.courses["some name"] = ["1", "2"]

		self.assertEqual({"some name":  ["1", "2"]}, self.student.courses)

		result = self.student.add_notes("some name", "new data")

		self.assertEqual({"some name":  ["1", "2", "new data"]}, self.student.courses)
		self.assertEqual("Notes have been updated", result)

	def test_add_notes_method_course_not_in_courses(self):
		with self.assertRaises(Exception) as ex:
			self.student.add_notes("some name", "new data")

		self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

	def test_leave_course_course_in_courses(self):
		self.student.courses["some name"] = []

		result = self.student.leave_course("some name")

		self.assertEqual({}, self.student.courses)
		self.assertEqual("Course has been removed", result)

	def test_leave_course_course_not_in(self):
		with self.assertRaises(Exception) as ex:
			self.student.leave_course("some name")

		self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
	main()
