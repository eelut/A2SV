# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque

def bfs(graph, n):
    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist[n]

n, m = map(int, input().split())
rail = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    rail[u][v] = rail[v][u] = True

rail_graph = [[] for _ in range(n + 1)]
road_graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            if rail[i][j]:
                rail_graph[i].append(j)
            else:
                road_graph[i].append(j)

if rail[1][n]: 
    train_graph = rail_graph
    bus_graph = road_graph
else:
    train_graph = road_graph
    bus_graph = rail_graph

train_dist = bfs(train_graph, n)
bus_dist = bfs(bus_graph, n)

if train_dist == -1 or bus_dist == -1:
    print(-1)
else:
    print(max(train_dist, bus_dist))
