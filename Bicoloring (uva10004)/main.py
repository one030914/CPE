from collections import deque

while True:
    n = int(input())
    if n == 0: break
    
    l = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(l):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [-1] * n
    is_bipartite = True

    queue = deque()
    queue.append(0)
    color[0] = 0

    while queue and is_bipartite:
        node = queue.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                is_bipartite = False
                break

    print("BICOLORABLE." if is_bipartite else "NOT BICOLORABLE.")