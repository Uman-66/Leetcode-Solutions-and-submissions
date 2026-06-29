class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        a.sort()
    
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                return True
            
        return False
