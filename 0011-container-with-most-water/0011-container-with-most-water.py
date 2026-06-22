class Solution:
    def maxArea(self, height: List[int]) -> int:
        l ,n = 0, len(height)
        r = n-1
        maxx = 0
        while(l<r):
            w = r-l
            h = min(height[l], height[r])
            cur = w*h
            maxx = max(cur, maxx)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxx