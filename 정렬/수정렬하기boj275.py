import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\구현\\input.txt")

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array.sort()

for i in range(len(array)):
    print(array[i])