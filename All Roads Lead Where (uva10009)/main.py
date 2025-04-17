def bfs(graph, start, end):
    queue = [start]
    visited = {start: None}

    while queue:
        curr = queue.pop(0)
        if curr == end:
            break
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited[neighbor] = curr
                queue.append(neighbor)

    path = []
    while end is not None:
        path.append(end)
        end = visited.get(end)
    path.reverse()
    return ''.join(city[0] for city in path)

t = int(input())
for test in range(t):
    space = input()
        
    n, q = map(int, input().split())
    graph = {}

    for _ in range(n):
        a, b = input().split()
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    for _ in range(q):
        a, b = input().split()
        print(bfs(graph, a, b))

