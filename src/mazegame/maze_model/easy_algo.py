#!/usr/bin/env python
# coding=utf-8
def generate_maze(width=10, height=10):
    maze = [["#" for _ in range(width)] for _ in range(height)]
    
    for i in range(height-1):
        maze[i][1] = " "
    
    for j in range(1, width):
        maze[i][j] = " "
    
    return maze, (0,1), (height-2,width-1)

def print_maze(maze):
    for row in maze:
        print(*row)

if __name__ == '__main__':
    grid, start, end = generate_maze(3,4)
    print_maze(grid)
    print(start, end)