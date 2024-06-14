class Mystack:
    def __init__(self) -> None:
        self._data = []
        self._data.append(dat)

    def push(self, data):
        self._data.pop()

        pass

    def peek(self):
        if self._data:
            return self._data[-1]
        else:
            return None
