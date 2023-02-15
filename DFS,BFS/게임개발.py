import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt", "r")

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n,m = map(int, input().split())

d = [[0]*m for _ in range(n)]
x,y, dir = map(int, input().split())
d[x][y] = 1

array = []

for i in range(n):
    array.append(list(map(int,input.split())))
