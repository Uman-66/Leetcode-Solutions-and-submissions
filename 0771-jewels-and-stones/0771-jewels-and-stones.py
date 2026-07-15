class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_set = set(jewels)
        count = 0
        for i in stones:
            if i in j_set:
                count+=1
        return count