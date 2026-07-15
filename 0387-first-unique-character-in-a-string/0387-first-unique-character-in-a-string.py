class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, ch in enumerate(s):
            if s.count(ch) == 1:
                return i
        return -1