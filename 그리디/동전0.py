import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

n,k = map(int,input().split())

change = []
for i in range(n):
    change.append(int(input()))

change.sort(reverse=True)
cnt = 0

while k!=0:
    for i in change:
        if k >= i:
            cnt += k//i
            k = k%i
    
print(cnt)