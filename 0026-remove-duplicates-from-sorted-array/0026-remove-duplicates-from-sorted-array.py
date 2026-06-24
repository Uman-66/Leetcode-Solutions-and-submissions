class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != k:
                k = nums[i]
            else:
                nums.pop(i)
        return len(nums)
        