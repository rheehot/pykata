class MultipleIterator:
    def __init__(self, stop, multiple):
        self._stop = stop
        self._multiple = multiple
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._current += 1
        if self._current * self._multiple < self._stop:
            return self._current * self._multiple
        else:
            raise StopIteration


for i in MultipleIterator(20, 3):
    print(i)