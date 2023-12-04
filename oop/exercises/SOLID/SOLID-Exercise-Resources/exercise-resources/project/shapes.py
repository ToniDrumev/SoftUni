from abc import ABC, abstractmethod


class Area(ABC):

    @abstractmethod
    def area(self):
        ...


class Rectangle(Area):

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


class Triangle(Area):

    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return self.base * self.height / 2


class Circle(Area):
    PI = 3.14

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self) -> float:
        return self.PI * self.radius ** 2


class AreaCalculator:

    def __init__(self, shapes):

        if not isinstance(shapes, list):
            print("`shapes` should be of type `list`.")
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total


shapes = [Rectangle(2, 3), Triangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes.append(Circle(3))

print("The total area is: ", calculator.total_area)
