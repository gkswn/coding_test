import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\정렬\\input.txt")

n = int(input())
array = []

for i in range(n):
    start, end = map(int, input().split())
    array.append([start, end])
print(array)
array = sorted(array, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
print(array)
array = sorted(array, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
print(array)
last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in array:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)