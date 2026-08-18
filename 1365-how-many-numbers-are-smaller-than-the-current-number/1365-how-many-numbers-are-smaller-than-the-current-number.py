from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort the array to know the order
        sorted_nums = sorted(nums)
        
        # Map each value to its first index in the sorted array
        # That index is exactly the number of elements smaller than it
        smaller_count = {}
        for i, val in enumerate(sorted_nums):
            if val not in smaller_count:   # keep the smallest index (first occurrence)
                smaller_count[val] = i
        
        # Build the answer by looking up each element
        return [smaller_count[x] for x in nums]