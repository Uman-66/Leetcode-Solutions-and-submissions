class Solution:
    def allsubsets(self, nums: List[int], ans: List[int], i: int, alll: List[List[int]]):
        if i == len(nums):
            alll.append(ans[:])
            return

        ans.append(nums[i])
        self.allsubsets(nums, ans, i+1, alll)
        ans.pop()
        idx = i+1
        while (idx<len(nums) and nums[idx-1]==nums[idx]):
            idx+=1

        self.allsubsets(nums, ans, idx, alll)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        alll = []
        nums.sort()
        ans = []
        self.allsubsets(nums, ans, 0 ,alll)
        return alll