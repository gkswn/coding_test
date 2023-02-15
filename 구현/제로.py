import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\구현\\input.txt")

n = int(input())

array = []

for i in range(n):
    num = int(input())
    if num != 0:
        array.append(num)
    else:
        array.pop(-1)

result = sum(array)
print(result)