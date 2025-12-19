import random

WALL = 1
PASSAGE = 0

class Maze:
    def __init__(self, width: int, height: int):
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.grid = [[WALL for _ in range(self.width)] for _ in range(self.height)]

    def generate(self, start=(1, 1)):
        sr, sc = start
        self.grid[sr][sc] = PASSAGE

        stack = [(sr, sc)]
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        while stack:
            r, c = stack[-1]
            random.shuffle(directions)

            carved = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 1 <= nr < self.height - 1 and 1 <= nc < self.width - 1:
                    if self.grid[nr][nc] == WALL:
                        self.grid[r + dr // 2][c + dc // 2] = PASSAGE
                        self.grid[nr][nc] = PASSAGE
                        stack.append((nr, nc))
                        carved = True
                        break

            if not carved:
                stack.pop()
