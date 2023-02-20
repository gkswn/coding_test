from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

m,n,h = map(int, input().split())

graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

answer = 0

def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if nx<0 or ny<0 or nz<0 or nx>=h or ny >=n or nz >= m:
                continue
            if graph[nx][ny][nz] == 0 and not visit[nx][ny][nz]:
                queue.append((nx,ny,nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visit[nx][ny][nz] = True

for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1 and visit[a][b][c] == 0:
                queue.append((a,b,c))
                visit[a][b][c] = True
bfs()

# 토마토 확인

for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        answer = max(answer, max(b))

print(answer-1)