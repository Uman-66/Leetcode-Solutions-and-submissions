from typing import List

class Solution:
    def getPerms(self, nums: List[int], idx: int, ans: List[List[int]]):
        if idx == len(nums):
            ans.append(nums[:])          # copy the current permutation
            return

        for i in range(idx, len(nums)):
            # swap to place nums[i] at position idx
            nums[idx], nums[i] = nums[i], nums[idx]
            self.getPerms(nums, idx + 1, ans)
            # backtrack: swap back
            nums[idx], nums[i] = nums[i], nums[idx]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.getPerms(nums, 0, ans)
        return ans