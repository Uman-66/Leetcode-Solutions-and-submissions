class Solution:
    def Valid(self, piles: List[int], h: int, k: int) -> bool:
        total_hours = 0
        for n in piles:
            total_hours+=(n+k-1)//k
            if total_hours>h:
                return False
        return total_hours<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st = 1
        end = max(piles)
        ans = end

        while st<=end:
            mid=st+(end-st)//2
            if self.Valid(piles, h, mid):
                ans=mid
                end= mid-1
            else:
                st = mid+1

        return ans