class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        nums = int("".join(map(str, a)))
        nums= nums+1
        return [int (d) for d in str(nums)]