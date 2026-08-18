from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store next greater element for each value in nums2
        next_greater = {}
        stack = []  # monotonic decreasing stack (strictly decreasing from bottom to top)

        # Traverse nums2 from right to left
        for i in range(len(nums2) - 1, -1, -1):
            # Pop elements that are <= current, because they cannot be the next greater for any earlier element
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            # After popping, the top of the stack is the next greater element (or None)
            if not stack:
                next_greater[nums2[i]] = -1
            else:
                next_greater[nums2[i]] = stack[-1]

            # Push current element onto the stack
            stack.append(nums2[i])

        # Build the answer for nums1 using the map
        ans = []
        for num in nums1:
            ans.append(next_greater[num])

        return ans