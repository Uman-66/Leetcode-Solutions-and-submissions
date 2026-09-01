from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque()  # will store indices

        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            # Add current index
            dq.append(i)

            # When the first window is complete, record the maximum
            if i >= k - 1:
                output.append(nums[dq[0]])

        return output
        