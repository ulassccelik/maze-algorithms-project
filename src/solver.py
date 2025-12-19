from collections import deque

WALL = 1

def bfs_solve(grid, start, goal):
    sr, sc = start
    gr, gc = goal

    if grid[sr][sc] == WALL or grid[gr][gc] == WALL:
        return None

    q = deque([start])
    parent = {start: None}
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        r, c = q.popleft()
        if (r, c) == goal:
            return _reconstruct_path(parent, goal)

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] != WALL and (nr, nc) not in parent:
                    parent[(nr, nc)] = (r, c)
                    q.append((nr, nc))

    return None

def _reconstruct_path(parent, end):
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
