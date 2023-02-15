import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt", encoding= 'utf-8')

n = int(input())

array = []

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))


a = []
for i in range(n):
    a = array[1]
    a.sort()
    

    
for student in array:
    print(student[0], end=' ')