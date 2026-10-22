
class Solution:
    def rearrangeArray(self, nums: nums[int]) -> list[int]:
        pos = 0
        neg = 1
        new = [0] * len(nums)
        for i in range (0,len(nums)):
            if nums[i] >= 0:
                new[pos] = nums[i]
                pos = pos + 2
            else:
                new[neg] = nums[i]
                neg = neg + 2
        return new