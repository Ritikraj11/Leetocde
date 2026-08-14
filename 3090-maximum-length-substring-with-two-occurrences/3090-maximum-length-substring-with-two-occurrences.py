class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # If current character occurs more than 2 times
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            # Current window is valid
            ans = max(ans, right - left + 1)

        return ans