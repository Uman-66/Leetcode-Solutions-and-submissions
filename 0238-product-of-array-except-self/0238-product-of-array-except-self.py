class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            suffix *= nums[j+1]

            ans[j] *= suffix
        return ans
        