class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # prefix sum
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # If Alice merges ALL stones:
        ans = prefix[n - 1]

        # Try stopping the first merge earlier.
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans