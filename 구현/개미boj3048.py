import sys
sys.stdin = open('C:\\Users\\안한주\\Desktop\\coding_test\\구현\\input.txt')

n1, n2 = map(int, input().split())

ant1 = list(map(str,sys.stdin.readline().rstrip("\n")))
ant2 = list(map(str,sys.stdin.readline().rstrip("\n")))
t = int(input())
ant1.reverse()
total = ant1 + ant2

for _ in range(t):
    for i in range(len(total)-1):
        if total[i] in ant1 and total[i+1] in ant2:
            total[i], total[i+1] = total[i+1] , total[i]

            if total[i+1] == ant1[-1]:
                break

print("".join(total))