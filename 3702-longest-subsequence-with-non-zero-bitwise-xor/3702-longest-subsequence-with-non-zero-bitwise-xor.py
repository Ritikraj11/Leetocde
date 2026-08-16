class Solution:
    def longestSubsequence(self, nums):
        totalXor = 0
        hasNonZero = False

        for num in nums:
            totalXor ^= num

            if num != 0:
                hasNonZero = True

        if totalXor != 0:
            return len(nums)

        if hasNonZero:
            return len(nums) - 1

        return 0