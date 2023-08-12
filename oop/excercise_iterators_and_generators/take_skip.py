class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self.current

        if i < self.count:
            self.current += 1

            return i * self.step

        else:
            raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
 print(number)