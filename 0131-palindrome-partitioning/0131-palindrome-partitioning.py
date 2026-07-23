class Solution:
    def ispalin(self, s):
        
        return s[::-1] == s
            
    def gal(self, s, partitions, ans):
        if len(s) == 0:
            ans.append(partitions[:])
            return
        for i in range(len(s)):
            part = s[0:i+1]
            if self.ispalin(part):
                partitions.append(part)
                self.gal(s[i+1:], partitions, ans)
                partitions.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partitions = []
        self.gal(s, partitions, ans)
        return ans