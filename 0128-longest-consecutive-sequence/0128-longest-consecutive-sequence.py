class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if(len(nums) == 0):
            return 0
        my_set = set()
        for i in range(0,len(nums)):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num - 1 not in my_set:
                start = num
                count = 0
                while start in my_set:
                    count =count + 1 
                    start =start + 1
                longest = max(longest,count)
        return (longest)