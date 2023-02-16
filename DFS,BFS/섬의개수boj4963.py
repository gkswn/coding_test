from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")
sys.setrecursionlimit(10000)

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]


def dfs(x,y):
    visit[x][y] = 1
    if graph[x][y]==1:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx<h and 0<=ny<w:
                if graph[nx][ny]==1 and not visit[nx][ny]:
                    dfs(nx,ny)
    return 1

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    answer = 0
    graph = []
    visit = [[0]*w for _ in range(h)]
    
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if not visit[i][j] and graph[i][j] == 1:
                dfs(i,j)
                answer += 1
            else:
                continue

    print(answer)