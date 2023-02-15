from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

n = int(input())
m = int(input())
computer=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    computer[a][b] = 1
    computer[b][a] = 1

visit=[0]*(n+1)
queue = deque()
queue.append(1)
visit[1] = 1
cnt = 0

while queue:
    now = queue.popleft()
    for i in range(1, n+1):
        if computer[now][i] ==1 and visit[i] ==0:
            visit[i] = 1
            queue.append(i)
            cnt+=1

print(cnt)