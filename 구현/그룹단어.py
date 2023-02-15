import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\구현\\input.txt")

n=int(input())

for i in range(n):
    a=list(input())
    for j in range(len(a)-1): 
        if a[j]==a[j+1]: 
            pass
        elif a[j] in a[j+2:]:
            n-=1
            break
print(n)