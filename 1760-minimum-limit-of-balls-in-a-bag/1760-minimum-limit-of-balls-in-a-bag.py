class Solution:
    def Valid(self, nums: List[int], maxOperations: int, target: int) -> bool:
        total_ops = 0
        for n in nums:
            pieces = (n + target - 1) // target   # ceil(n / target)
            total_ops += pieces - 1
            if total_ops > maxOperations:
                return False
        return True

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        st = 1
        end = max(nums)
        ans = end

        while st <= end:
            mid = st + (end - st) // 2
            if self.Valid(nums, maxOperations, mid):
                ans = mid
                end = mid - 1
            else:
                st = mid + 1

        return ans