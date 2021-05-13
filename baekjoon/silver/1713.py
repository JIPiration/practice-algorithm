from collections import deque

deque = deque() # deque()
n = int(input())
m = int(input())
array = list(map(int, input().split()))
bucket = [0 for i in range(m)]

for i in array:
    if i in deque:    
        bucket[i-1] += 1
    elif (i not in deque) and (len(deque) < 3):
        deque.append(i)
        bucket[i-1] = 1
    else:
        num = 0
        while bucket[i-1] + 1 >= bucket[deque[num]-1]:
            if bucket[i-1] + 1 == bucket[deque[num]-1]:
                bucket[deque[num]-1] = 0
                bucket[i-1] = 1
                deque.popleft()
                deque.append(i)
                break
            num += 1

# sorting
array = { deque[num]:bucket[deque[num]-1] for num in range(n) }
sarray = sorted(array.items(), reverse=False)
result = [i[0] for i in sarray]
print(result)
