class Solution:
    def allsubset(self, nums: List[int], ans: List[int], i: int, a: List[List[int]]):
        if i == len(nums):
            a.append(ans[:])
            return
        ans.append(nums[i])
        self.allsubset(nums,ans, i+1, a)
        ans.pop()
        self.allsubset(nums,ans, i+1, a)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        alll = []
        ans = []
        self.allsubset(nums, ans, 0,alll)
        return alll