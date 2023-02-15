from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

n,m = map(int, input().split())

array = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # 4방향 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx >=n or ny>=m:
                continue
            if array[nx][ny]==0:
                continue
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y]+1
                queue.append((nx,ny))

    return array[n-1][m-1]

print(bfs(0,0))