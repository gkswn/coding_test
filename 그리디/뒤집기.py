import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

a = input()

a0 = a.split('0')
a1 = a.split('1')


cnt0 = 0
cnt1 = 0

for i in a0:
    if '1' in i:
        cnt0 +=1


for i in a1:
    if '0' in i:
        cnt1 +=1

print(min(cnt0, cnt1))