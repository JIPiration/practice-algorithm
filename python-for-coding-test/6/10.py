
n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

# 파이썬 정렬 라이브러리를 이용하여 내림차순 정렬 수행
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
