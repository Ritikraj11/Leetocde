class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # mini = min(prices)
        # min_idx = prices.index(mini)
        # maxi = prices[min_idx]

        # for i in range(min_idx,len(prices)):
        #     if(prices[i] > maxi):
        #         maxi = prices[i]

        # diff = maxi - mini
        # if(diff <= 0):
        #     return 0
        # else:
        #     return diff

        maxi = 0
        mini = float("inf")
        n = len(prices)

        for i in range(0,n):
            mini = min(mini,prices[i])
            maxi = max(maxi, prices[i] - mini)

        return maxi