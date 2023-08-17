"""
STACK data structure - Last In, First Out
Based on python's LIST sequence
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):  # Removes a value and returns it
        return self.items.pop()

    def peek(self):  # Returns last item in the stack
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):  # Gives more info on class instances when we print it
        return str(self.items)


if __name__ == "__main__":  # Convention for not executing this bit if imported as a module
    s = Stack()  # Classes start with capital letters, objects with small ones
    print(s)
    print(s.is_empty())
    s.push(1)
    print(s)
    print(s.is_empty())
    s.push(3)
    s.push(8)
    print(s)
    print(s.pop())  # removes a value and returns it
    print(s)
