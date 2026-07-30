class Solution(object):
    def subsets(self, arr):
        result = []

        def print_subsets(arr, ans, i):
            if i == len(arr):
                result.append(ans[:])
                return
            ans.append(arr[i])
            print_subsets(arr, ans, i+1)
            ans.pop()
            print_subsets(arr, ans, i+1)

        print_subsets(arr, [], 0)
        return result