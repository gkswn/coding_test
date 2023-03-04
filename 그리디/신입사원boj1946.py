import sys
sys.stdin = open('C:\\Users\\안한주\\Desktop\\coding_test\\그리디\\input.txt')

t = int(input())


for i in range(t):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(map(int,input().split())))
    arr.sort()
    top = 0
    result = 1

    for i in range(1, len(arr)):
        if arr[i][1]<arr[top][1]:
            top = i
            result += 1
    print(result)
