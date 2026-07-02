class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = i % 10
            if ( a == nums[i]):
                return i
        return -1