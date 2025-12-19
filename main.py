from src.maze import Maze
from src.solver import bfs_solve
from src.utils import render_maze

def main():
    width, height = 21, 11
    maze = Maze(width=width, height=height)
    maze.generate()

    start = (1, 1)
    goal = (maze.height - 2, maze.width - 2)

    path = bfs_solve(maze.grid, start, goal)

    print("Maze Algorithms Project")
    print("Author: Ulaş Çelik (200021858)\n")

    if path:
        print("Solution found!\n")
        print(render_maze(maze.grid, path=path, start=start, goal=goal))
        print(f"\nPath length: {len(path)}")
    else:
        print("No solution found.")
        print(render_maze(maze.grid, start=start, goal=goal))

if __name__ == "__main__":
    main()
