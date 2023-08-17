"""
PRIORITY QUEUE data structure - First In, Priority Out :D (Edoc out of hours service queue)
Based on python's HEAPQ (heap queue algorithm)
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, priority, item):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority
    pq.put(2, "eat")
    pq.put(1, "code")
    pq.put(3, "sleep")
    print(pq)
    print(pq.get())
    print(pq.get())
    print(pq.get())
