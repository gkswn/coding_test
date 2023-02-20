from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 1
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny] == 1 and visit[nx][ny] == False:
                    cnt +=1
                    visit[nx][ny] = True
                    queue.append((nx,ny))
    return cnt 
                              
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
result = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] == False:
            visit[i][j] = True
            result.append(bfs(i,j))

print(len(result))
print(max(result) if result else 0)