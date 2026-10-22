import math
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        frq = {}
        exact = math.ceil(len(nums)/2)
        for num in nums:
            frq[num] = frq.get(num,0)+1
        for k,v in frq.items():
            if v >= exact:
                return k