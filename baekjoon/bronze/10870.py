n = int(input())
pivo_list = [0, 1]

# 1. for문
for i in range(2, n+1):
    pivo_num = pivo_list[i-1] + pivo_list[i-2]
    pivo_list.append(pivo_num)

print(pivo_list[n])




