import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

a = input().split('-')

num = []

for i in a:
    cnt = 0
    s = i.split("+")
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -=num[i]

print(n)