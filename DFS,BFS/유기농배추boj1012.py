import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < m) and (0 <= ny < n):
            if array[ny][nx] == 1:
                array[ny][nx] = -1
                dfs(nx, ny)
t = int(input())


for i in range(t):
    m,n,k = map(int, input().split())
    array = [[0]*m for _ in range(n)]
    cnt = 0 
    
    for x in range(k):
        a,b = map(int, input().split())
        array[b][a] = 1

    for i in range(m):
        for j in range(n):
            if array[j][i] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)