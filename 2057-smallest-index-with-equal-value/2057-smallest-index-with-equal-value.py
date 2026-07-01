class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            ans = i%10
            if(ans==nums[i]):
                return i
        return -1