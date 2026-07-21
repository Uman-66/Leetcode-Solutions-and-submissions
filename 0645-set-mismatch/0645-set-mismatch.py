from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n + 1)
        for num in nums:
            freq[num] += 1

        ans = [0, 0]
        for i in range(1, n + 1):
            if freq[i] == 2:
                ans[0] = i         
            elif freq[i] == 0:
                ans[1] = i          
        return ans