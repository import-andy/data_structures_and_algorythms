"""
Breadth First Search (BFS) aka FLOODING.
Based on the QUEUE data structure - First In - First Out (people in queue).

HOW I UNDERSTAND IT WORKS:
1. it checks for the surrounding nodes in a CLOCKWISE direction
2. it goes to the FIRST of ALL detected nodes (first in - first out), NOT for
that just have been detected during last move

The queue contains positions as (row, column) tuples.
Predecessors are kept as a {position: predecessors} pair in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from queue_xx import Queue


def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ['up', 'right', 'down', 'left']:  # Clockwise
            row_offset, col_offset = offsets[direction]
            neighbour = (row_offset + current_cell[0], col_offset + current_cell[1])
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell  # This is how to add to a dictionary

    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
