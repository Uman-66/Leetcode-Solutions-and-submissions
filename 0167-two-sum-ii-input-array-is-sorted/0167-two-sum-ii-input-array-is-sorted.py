class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i =0
        j = n-1
        ans = []
        while(i<j):
            summ = numbers[i] + numbers[j]
            if (summ == target):
                ans.append(i+1)
                ans.append(j+1)
                break
            elif(summ > target):
                j=j-1
            elif(summ < target):
                i=i+1

        return ans


        