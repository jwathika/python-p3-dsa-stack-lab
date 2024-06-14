class Stack:

    def __init__(self, items=[], limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit or self.isEmpty():
            self.items.append(item)
        else:
            return "Stack is full"

    def pop(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def peek(self):
        if self.isEmpty():
            return None
        else:
            self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return None

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return i
            else:
                return None
        return -1
