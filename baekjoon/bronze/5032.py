a, b, c = map(int, input().split())

results = 0
n = a + b

while n >= c:
    quotient, remain = divmod(n, c)
    results += quotient
    n = quotient + remain

print(results)
