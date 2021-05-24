from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        summ = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어 합 계산
            pair.append(n)
            if len(pair) == 2:
                summ += min(pair)
                pair = []

        return summ
