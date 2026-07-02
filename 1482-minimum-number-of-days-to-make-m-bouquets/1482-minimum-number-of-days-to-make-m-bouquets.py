class Solution:
    def isValid(self, a: List[int], m: int, k: int, mid: int) -> bool:
        b = 0
        c = 0
        for days in a:
            if days <= mid:
                c += 1
            else:
                b += c // k
                c = 0
        b += c // k
        if b >= m:
            return True
        return False




    def minDays(self, bloomday: List[int], m: int, k: int) -> int:
        if m*k > len (bloomday):
            return -1


        s = min(bloomday)
        e = max(bloomday)
        ans = 0
        while s <= e:
            mid = s + (e-s)//2
            t = self.isValid(bloomday, m, k, mid)
            if t:
                ans = mid
                e = mid-1
            else:
                s = mid + 1
        return ans