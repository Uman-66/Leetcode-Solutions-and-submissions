class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        e = len(s)-1
        while(st<e):
            while (st<e) and not s[st].isalnum():
                st+=1
            while (st<e) and not s[e].isalnum():
                e-=1
            if s[st].lower() != s[e].lower():
                return False
            st+=1
            e-=1
        return True