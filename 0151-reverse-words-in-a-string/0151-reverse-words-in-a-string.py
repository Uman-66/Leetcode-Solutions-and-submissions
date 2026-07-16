class Solution:
    def reverseWords(self, s: str) -> str:
        s= s[::-1]
        ans = ''
        n = len(s)
        i = 0
        while i < n:
            while i < n and  s[i] == ' ':
                i += 1
            if i >=n:
                break
            word = ''
            while i < n and s[i] != ' ':
                word+=s[i]
                i+=1
            word = word[::-1]
            
            if len(word)>0:
                if ans:
                    ans += " "
                ans += word
        return ans
