class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        ans = 0
        for i in range(len(nums)):
            if(freq == 0):
                ans = nums[i]
            if(nums[i] == ans):
                freq += 1
            else:
                freq -= 1

        return ans