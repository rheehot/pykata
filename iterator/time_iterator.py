class TimeIterator:
    def __init__(self, start, stop):
        self._start = start
        self._stop = stop

    def __getitem__(self, index):
        if index < self._stop - self._start:
            return self._transform(self._start + index)
        else:
            raise IndexError

    def _transform(self, second):
        hour, minute = divmod(second, 3600)
        minute, second = divmod(minute, 60)
        
        hour %= 24
        return '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)


for i in TimeIterator(88234, 88237):
    print(i)

print(TimeIterator(88234, 88237)[2])