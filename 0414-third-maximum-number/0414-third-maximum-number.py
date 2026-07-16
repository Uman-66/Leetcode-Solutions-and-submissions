class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        d = set(nums)
        if len(d)<3:
            return max(d)
        array = sorted(d, reverse = True)
        return array[2]