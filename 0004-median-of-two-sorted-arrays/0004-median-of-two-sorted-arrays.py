class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i =j = 0
        arr = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j+=1
            else:
                arr.append(nums1[i])
                arr.append(nums2[j])
                i += 1
                j += 1
        while i < m:
            arr.append(nums1[i])
            i+=1
        while j < n:
            arr.append(nums2[j])
            j += 1
        x = len(arr)
        if x%2 == 0:
            return (arr[x//2-1] + arr[x//2])/2
        else:
            return arr[x//2]

        