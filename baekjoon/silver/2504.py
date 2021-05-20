from collections import deque
from typing import Deque

array = list(map(str, input()))
#deq: Deque = deque()
dic = {')': '(',
        ']': '['}

result = 0
num = 1
math_bol = False

#while num < len(array):
#for i in range(1, len(array)):

while num <= len(array):
    num_each = 1
    math_bol = False

    while array[num] in dic and (array[num-1] == dic[array[num]]):
        if array[num] == ')':
            num_each *= 2
        elif array[num] == ']':
            num_each *= 3
        array.pop(num)
        array.pop(num-1)
        num -= 1

        math_bol = True
        if len(array) <= 0:
            break

    num += 1
    if math_bol:
        result += num_each

print("result: ", result)
