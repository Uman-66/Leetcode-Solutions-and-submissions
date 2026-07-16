class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        n = len(a)
        count = 0
        prefixsum = [0]*n
        prefixsum[0] = a[0]
        for i in range(1,n):
            prefixsum[i] = prefixsum[i-1] + a[i]
        m = {}
        for j in range(n):
            if prefixsum[j]==k:
                count +=1

            val = prefixsum[j] - k
            if val in m:
                count += m[val]
            m[prefixsum[j]] = m.get(prefixsum[j], 0)+1
        return count