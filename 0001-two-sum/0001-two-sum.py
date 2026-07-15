class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isin = {}
        for i, num in  enumerate(nums):
            second = target - num
            if second in isin:
                return[isin[second], i]

            isin[num] = i
        return 0