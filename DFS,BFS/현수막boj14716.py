from collections import deque
import sys
sys.setrecursionlimit(100000)
sys.stdin = open('C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt')

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
check = [[False]*n for _ in range(m)]
ans = 0

def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if not check[nx][ny] and a[nx][ny]:
            dfs(nx, ny)

for i in range(m):
    for j in range(n):
        if not check[i][j] and a[i][j]:
            dfs(i, j)
            ans += 1
print(ans)