class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = (2*len(nums))-1
        stack = []
        ans = [-1]*n
        for i in range(m, -1, -1):
            while stack and nums[i%n] >= stack[-1]:
                stack.pop()
            if not stack:
                ans[i%n] = -1
            else:
                ans[i%n] = stack[-1]           
            stack.append(nums[i%n])

        return ans