from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return piles[i]

            left = piles[i] - dp(i + 1, j)
            right = piles[j] - dp(i, j - 1)

            return max(left, right)

        return dp(0, len(piles) - 1) >= 0