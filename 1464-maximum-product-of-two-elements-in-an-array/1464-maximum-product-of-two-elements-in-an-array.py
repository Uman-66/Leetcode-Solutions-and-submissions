class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = float("-inf")
        min1 = min2 = float("inf")
        for i in nums:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
            if i < min1:
                min2 = min1
                min1 = i
            if i < min2:
                min2 = i
        return max((max1-1)*(max2-1), (min1-1) * (min2-1))