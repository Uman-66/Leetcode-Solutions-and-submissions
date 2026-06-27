class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        st  = 0
        end = len(nums)-1
        mid = 0
        
        while(st<= end):
            mid = st + (end-st)//2
            if mid == 0:
                return nums[mid]
            if mid == len(nums)-1:
                return nums[mid]
            if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
                return nums[mid]
            elif(mid %2 == 0):
                if(nums[mid] == nums[mid-1]):
                    end = mid-1
                else:
                    st = mid+1
            else:
                if(nums[mid] == nums[mid-1]):
                    st = mid+1
                else:
                    end = mid - 1
