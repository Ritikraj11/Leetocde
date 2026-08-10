from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):

            # No piles left
            if i == n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):

                taken_by_opponent = dp(
                    i + X,
                    max(M, X)
                )

                current_player = suffix[i] - taken_by_opponent

                best = max(best, current_player)

            return best

        return dp(0, 1)