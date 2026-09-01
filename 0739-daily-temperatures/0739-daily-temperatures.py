from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # stores indices of temperatures (decreasing)

        for i in range(n - 1, -1, -1):
            # Pop while the current temperature is >= the temperature at stack top
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            # If stack is not empty, the top is the nearest warmer day
            if stack:
                ans[i] = stack[-1] - i
            # Push current index
            stack.append(i)

        return ans