import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

time = [300, 60, 10]

t = int(input())
cnt = []


for i in range(3):
    if t>=time[i]:
        cnt.append(t//time[i]) 
        t = t%time[i]

    elif t< time[i]:
        cnt.append(0)
        
    
if t == 0:
    result = ' '.join(str(i) for i in cnt)
    print(result)
else:
    print(-1)
