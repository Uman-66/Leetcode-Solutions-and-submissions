class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        if len(s1) > len(s2):
            return False
        for ch in s1:
            freq[ord(ch) - ord("a")]+=1
        
        window = [0]*26
        for i in range(len(s2)):
            window[ord(s2[i]) - ord("a")]+=1
            if i >=len(s1):
                left_char = s2[i-len(s1)]
                window[ord(left_char) - ord("a")] -= 1
        
            if window == freq:
                return True

        return False