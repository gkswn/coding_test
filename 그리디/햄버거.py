import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

n,k = map(int,input().split())

hp = list(input())
cnt = 0

for i in range(len(hp)):
    if hp[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0<=j<n and hp[j]=='H':
                cnt+=1
                hp[j] = 'E'
                break

print(cnt)