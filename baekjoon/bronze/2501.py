# 1.
n, m = list(map(int, input().split()))
result = []

for i in range(n):
    if n % (i+1) == 0:
        result.append(i+1)

if len(result) < m:
    print(0)
else:
    print(result[m-1])
