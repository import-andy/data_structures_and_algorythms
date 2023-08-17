"""
A* algorythm.
Based on the PRIORITY QUEUE data structure - First In, Priority Out :D

HOW I UNDERSTAND IT WORKS:
- it chooses the best next node to visit based on it's distance from a start and distance to a goal

G value - start to current node distance
H value - current node to destination distance (heuristic)
F value - sum of G & H values

Priority queue contains priority (F values) and (i, j) tuples;
Predecessors are kept as a {position: predecessors} pair in a dictionary.
G values are kept as a {position: g_value} pair in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):  # Calculates current node to destination distance.
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(0, start)  # Highest priority - it's a start
    predecessors = {start: None}  # position-predecessor pairs
    g_values = {start: 0}  # position-G value pairs

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ['up', 'right', 'down', 'left']:  # Clockwise order
            row_offset, coll_offset = offsets[direction]
            neighbour = (row_offset + current_cell[0], coll_offset + current_cell[1])
            if is_legal_pos(maze, neighbour) and neighbour not in g_values:  # 'not in g_values' - undiscovered
                """G value of new position will be guaranteed 1 cell further from start 
                because we are using an unweighted graph"""
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost  # Adding G value to dict
                f_value = new_cost + heuristic(neighbour, goal)
                pq.put(f_value, neighbour)
                predecessors[neighbour] = current_cell  # adding predecessor to dict
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
