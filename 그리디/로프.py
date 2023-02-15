import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
result = []
w = 0
num=1
for i in rope:
    w = i * num
    num += 1
    result.append(w)
maxw = max(result)

print(maxw)