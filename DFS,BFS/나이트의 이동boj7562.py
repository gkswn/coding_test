from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

t  = int(input())

def bfs(x,y):
    dx = [-2,-1,1,2,-2,-1,1,2]
    dy = [-1,-2,-2,-1,1,2,2,1]
    queue = deque()
    queue.append((x,y))
           
    while queue:
        x,y = queue.popleft()
        if x==tarx and y == tary:
            return graph[x][y]-1
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not graph[nx][ny]:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1

for i in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    nowx, nowy = map(int, input().split())
    tarx, tary = map(int, input().split())
    graph[nowx][nowy] = 1

    print(bfs(nowx, nowy))                