class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        na = []
        for i in range(0,n):
            if nums[i] != 0:
                na.append(nums[i])
        for i in range(0,len(na)):
            nums[i] = na[i]
        for i in range(len(na),n):
            nums[i] = 0
        
        