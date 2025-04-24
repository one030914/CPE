direct = [(-1, -1), (-1, 0), (-1, 1),
          (0, -1), (0, 1),
          (1, -1), (1, 0), (1, 1)]

def dfs(x, y, grid, m, n):
    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != '@':
        return
    grid[x][y] = '*'
    for dx, dy in direct:
        dfs(x + dx, y + dy, grid, m, n)

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0: break
    oil = [list(input()) for _ in range(m)]
    count = 0
    
    for i in range(m):
        for j in range(n):
            if oil[i][j] == '@':
                dfs(i, j, oil, m, n)
                count += 1
    print(count)