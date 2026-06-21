class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l ,r = 0, num
        mid = 0
        while (l <= r):
            mid = l + (r-l)//2
            if(mid*mid == num):
                return True
            if(mid*mid < num):
                l = mid+1
            elif(mid*mid > num):
                r = mid -1
        return False