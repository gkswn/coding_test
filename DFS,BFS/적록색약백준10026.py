from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
graph = [list(map(str,input().strip())) for _ in range(n)]

three_cnt, two_cnt = 0, 0

def bfs(x,y):
    visit[x][y] == True
    current_color = graph[x][y]
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny]== current_color and visit[nx][ny]==False:
                    visit[nx][ny] = True
                    queue.append((nx,ny))

# 아닌 경우
visit = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            bfs(i,j)
            three_cnt += 1


# 색맹인 경우
for i in range(n):
    for j in range(n):
        if graph[i][j] =='G':
            graph[i][j] = 'R'

visit = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            bfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)