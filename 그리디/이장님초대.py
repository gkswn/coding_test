import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

n = int(input())
tree = list(map(int, input().split()))

tree.sort(reverse=True)

max_day = 0
for i in range(n):
    cnt = tree[i] + i + 1
    if cnt > max_day:
        max_day = cnt

print(max_day+1)      