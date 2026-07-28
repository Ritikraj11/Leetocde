class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) % 2 == 0:
            mid = len(s) // 2
            part1 = s[:mid]
            strg = ''.join(sorted(part1))
            return strg + ''.join(reversed(strg))
        else:
            mid = len(s) // 2
            part1 = s[:mid]
            strg = ''.join(sorted(part1))
            return strg + s[mid] + ''.join(reversed(strg))