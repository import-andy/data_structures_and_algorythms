"""
QUEUE data structure - First In, First Out (aka Last In, Last out)
Based on python's DEQUE container
This file is not named "queue.py" because python has its own inbuilt module with such name.
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):  # Adds item to the end of deque
        self.items.append(item)

    def dequeue(self):  # Removes & returns the first item from the head of the queue
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):  # Returns the first item at the head of a queue
        return self.items[0]  # Taking the first element, not last

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue("1")
    q.enqueue("2")
    q.enqueue("3")
    print(q)
    print(q.dequeue())
    print(q)

