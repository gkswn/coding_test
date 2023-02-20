from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\완전탐색\\input.txt")

row, col = map(int, input().split())
board = [list(map(str,input().strip())) for _ in range(row)]
visit = [[False]*col for _ in range(row)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()    
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < col and 0 <= ny < row:
                if visit[nx][ny] == False:
                    pass

for i in row:
    for j in col:
        if board[i][j]:
            pass