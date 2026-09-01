class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i],0) + 1

        keys = list(hash.keys())
        for i in range(len(keys)):
            nums[i] = keys[i]
        return len(hash)