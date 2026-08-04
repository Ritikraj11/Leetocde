class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missingEl = []
        mini = min(nums)
        maxi = max(nums)
        for i in range(mini,maxi):
            if i not in nums:
                missingEl.append(i)

        return missingEl        