import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\완전탐색\\input.txt")

row, col = map(int, input().split())

cnt = 0
for i in range(row):
    array = list(input())
    for i in range(col):
        if array[i] == array[i+1] and i+1<=col:
            cnt += 1
        

print(cnt)