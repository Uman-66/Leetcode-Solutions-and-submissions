class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s = n+m
        a = m
        b = 0
        while(a != s and b < n):
            nums1[a] = nums2[b]
            a +=1
            b+=1

        nums1.sort()