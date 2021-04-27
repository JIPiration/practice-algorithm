# N, K
n, k = map(int, input().split())

result = 0  # 결과값: 실행 횟수

while(True):
    if n % k == 0:
        n /= k
        result += 1
    else:
        n -= 1
        result += 1

    if n == 1:
        break

print(result)
