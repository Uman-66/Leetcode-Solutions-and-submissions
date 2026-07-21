class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0] * 128          # enough for ASCII characters
        for ch in s:
            freq[ord(ch)] += 1

        ans = 0
        odd = False
        for count in freq:
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1
                odd = True

        if odd:
            ans += 1
        return ans