# class Solution:
#     def findMissingElements(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         missingEl = []
#         mini = min(nums)
#         maxi = max(nums)
#         for i in range(mini,maxi):
#             if i not in nums:
#                 missingEl.append(i)

#         return missingEl 

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []

        for i in range(len(nums) - 1):
            current = nums[i]
            nxt = nums[i + 1]

            while current + 1 < nxt:
                current += 1
                missing.append(current)

        return missing