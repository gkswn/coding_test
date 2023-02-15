import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt")

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

print(array)