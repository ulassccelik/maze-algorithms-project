WALL = 1

def render_maze(grid, path=None, start=None, goal=None):
    path_set = set(path) if path else set()
    lines = []
    for r in range(len(grid)):
        row_chars = []
        for c in range(len(grid[0])):
            ch = "#" if grid[r][c] == WALL else " "
            if (r, c) in path_set:
                ch = "."
            if start and (r, c) == start:
                ch = "S"
            if goal and (r, c) == goal:
                ch = "G"
            row_chars.append(ch)
        lines.append("".join(row_chars))
    return "\n".join(lines)
