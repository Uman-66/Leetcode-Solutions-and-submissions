class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            if (i > 0 and nums[i]==nums[i-1]):
                continue
            j = i+1
            k = n-1
            while(j<k):
                sum = nums[i]+nums[j]+nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j] == nums[j-1]):
                        j+=1    
        return ans