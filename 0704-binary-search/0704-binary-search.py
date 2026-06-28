class Solution:
    def search(self, a: List[int], target: int) -> int:
        s = 0
        e = len(a)-1
        mid = 0
        while(s<=e):
            mid = s + (e-s)//2
            if(a[mid] == target):
                return mid
            elif a[mid]< target:
                s = mid +1
            else:
                e = mid-1
        return -1