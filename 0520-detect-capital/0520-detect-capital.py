class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = sum(1 for ch in word if ch.isupper())
        return upper == len(word) or upper == 0 or (upper == 1 and word[0].isupper())