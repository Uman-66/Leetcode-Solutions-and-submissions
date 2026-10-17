class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iss = {}
        for i, num in enumerate(nums):
            second = target - num
            if second in iss:
                return [iss[second], i]
            iss[num] = i

        return 0