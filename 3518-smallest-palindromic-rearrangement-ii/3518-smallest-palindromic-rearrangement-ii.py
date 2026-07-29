from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = Counter()
        mid = ""

        for ch in freq:
            half[ch] = freq[ch] // 2
            if freq[ch] % 2:
                mid = ch

        m = sum(half.values())

        # factorials
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        # Initial permutation count
        total = fact[m]
        for v in half.values():
            total //= fact[v]

        if total < k:
            return ""

        left = []

        while m:

            for ch in sorted(half):

                if half[ch] == 0:
                    continue

                # permutations if we place ch here
                cnt = total * half[ch] // m

                if cnt >= k:
                    left.append(ch)
                    total = cnt
                    half[ch] -= 1
                    m -= 1
                    break
                else:
                    k -= cnt

        left = "".join(left)
        return left + mid + left[::-1]