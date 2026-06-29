class Solution:
    def Valid(self, position: List[int], m: int, mid : int) -> int:
        last = position[0]
        balls=1
        for i in range(1, len(position)):
            if position[i]-last < mid:
                continue
            else:
                balls +=1
                last = position[i]
        if balls >= m:
            return True
        else:
            return False

            
    def maxDistance(self, position: List[int], m: int) -> int:
        s = 1
        ans = 0
        position.sort()
        end = position[-1] - position[0]
        while(s<=end):
            mid = s + (end-s)//2
            v = self.Valid(position ,m, mid)
            if v:
                s = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans


