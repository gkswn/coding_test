import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt")

n = int(input())

change = [500,100,50,10,5,1]
money = 1000 - n

cnt =0

for i in change:
    if money >= i:
        cnt = money//i
        money %= i
print(cnt)
