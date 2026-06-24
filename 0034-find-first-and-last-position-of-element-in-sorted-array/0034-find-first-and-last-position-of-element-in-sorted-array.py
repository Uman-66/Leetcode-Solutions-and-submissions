class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        k = [-1, -1]
        for i in range(len(nums)):
            if(nums[i] == target):
                k[0] = i
                j = i
                while j+1<len(nums) and nums[j+1] == target:
                    j +=1
                k[1] = j
                break
        return k 