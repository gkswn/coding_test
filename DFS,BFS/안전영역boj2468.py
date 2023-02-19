from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
maxN = 0

for i in range(n):
    for j in range(n):
        maxN = max(maxN, graph[i][j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y,k):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny] == 0 and graph[nx][ny] >k:
                    visit[nx][ny] = 1
                    queue.append((nx,ny))
                    
result = []

for k in range(maxN):
    cnt = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>k and visit[i][j]==0:
                bfs(i,j,k)
                cnt += 1
    result.append(cnt)

print(max(result))