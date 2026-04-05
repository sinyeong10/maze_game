#!/usr/bin/env python
# coding=utf-8
import random

def make_kruskal(width=10, height=10):
    maze = [[1 for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]
    
    cells = []
    for r in range(height):
        for c in range(width):
            maze[2 * r + 1][2 * c + 1] = 0
            cells.append((r, c))

    walls = []
    for r in range(height):
        for c in range(width):
            if r < height - 1:
                walls.append(((r, c), (r + 1, c), (2 * r + 2, 2 * c + 1))) # 세로벽
            if c < width - 1:
                walls.append(((r, c), (r, c + 1), (2 * r + 1, 2 * c + 2))) # 가로벽
    
    random.shuffle(walls)

    parent = {cell: cell for cell in cells}

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    for cell1, cell2, wall_pos in walls:
        if union(cell1, cell2):
            maze[wall_pos[0]][wall_pos[1]] = 0

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(["#" if cell == 1 else " " for cell in row]))

if __name__ == '__main__':
    width, height = 2,1
    maze = make_kruskal(width, height)
    print(len(maze[0]), len(maze))
    print_maze(maze)