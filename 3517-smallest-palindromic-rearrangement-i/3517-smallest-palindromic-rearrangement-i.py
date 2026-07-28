class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Count frequency of each character
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Build the left half
        left = []
        for i in range(26):
            left.extend(chr(i + ord('a')) * (freq[i] // 2))

        # Find the middle character (if the length is odd)
        middle = ""
        for i in range(26):
            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))
                break

        # Convert left half to a string
        left = "".join(left)

        # Construct the palindrome
        return left + middle + left[::-1]