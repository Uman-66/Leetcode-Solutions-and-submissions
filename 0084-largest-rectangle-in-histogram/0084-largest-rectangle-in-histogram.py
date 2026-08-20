class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        l = [-1] *n
        r = [n] *n

        for i in range(len(heights)):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            l[i] = stack[-1] if stack else -1
            stack.append(i)
            

        stack.clear()
        for i in range(n-1, -1, -1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            r[i] = stack[-1] if stack else n

            stack.append(i)

        maxx= 0

        for i in range(len(heights)):

            w = r[i] - l[i] - 1

            area = heights[i] * w

            maxx = max( maxx, area)
        return maxx