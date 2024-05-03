"""
매번 탐색때마다 gen+=1

"""

from collections import deque


def bfs(graph, v):
    queue = deque(v)
    days = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 방향 상하좌우
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == 0:
                    graph[nr][nc] = 1
                    queue.append((nr, nc))
        days += 1

    # 토마토 다 익었는지 쳌
    for row in graph:
        if 0 in row:
            return -1
    return days - 1 if days > 0 else 0

col, row = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
v = [(i, j) for i in range(row) for j in range(col) if graph[i][j] == 1]

result = bfs(graph, v)
print(result)

