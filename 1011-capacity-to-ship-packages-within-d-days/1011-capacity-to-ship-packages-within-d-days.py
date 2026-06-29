class Solution:
    def Valid(self, w: List[int], days: int, minw : int) -> int:
        dy = 1
        wos = 0
        for i in range(len(w)):
            if(w[i] > minw):
                return False
            elif w[i]+wos <= minw:
                wos += w[i]
            else:
                wos = w[i]
                dy += 1
        if dy <= days:
            return True
        else:
            return False

    def shipWithinDays(self, w: List[int], days: int) -> int:
        end = 0
        ans = 0
        st = 0
        for i in range(len(w)):
            end += w[i]
            st = max(st, w[i])
        while(st<=end):
            mid = st + (end-st)//2
            v = self.Valid(w, days, mid)
            if not v:
                st = mid+1
                
            else:
                ans = mid
                end = mid-1
        return ans

