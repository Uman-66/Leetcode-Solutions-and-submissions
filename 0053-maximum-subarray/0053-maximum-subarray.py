class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxx =  float('-inf')

        for i in range(len(nums)):
            curr+=nums[i]
            maxx = max(curr, maxx)
            if(curr<0):
                curr = 0

        return maxx