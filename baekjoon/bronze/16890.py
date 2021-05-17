from collections import deque
from typing import List

n = list(map(str, input()))  # 구사과
m = list(map(str, input()))  # 큐트러버
company: List = list('?' * len(n))

# sort
deque_n, deque_m = deque(sorted(n, reverse=False)), deque(sorted(m, reverse=True))  # 오름차순, 내림차순
bol_n = True

for i in range(len(company)):
    #company[i] = str(i for i in if bol_n el)
    if bol_n:
        company[i] = deque_n.popleft()
        bol_n = False
    else:
        company[i] = deque_m.popleft()
        bol_n = True

company = ''.join(company)
print(company)
