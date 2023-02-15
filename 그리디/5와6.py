import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt")

a,b = map(int,input().split())

reA6 = str(a).replace('5','6')
reA5 = str(a).replace('6','5')

reB6 = str(b).replace('5','6')
reB5 = str(b).replace('6','5')

minab = int(reA5)+int(reB5)
maxab = int(reA6)+int(reB6)

print(minab, maxab)