class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        profit=0
        for i in prices:
            if i<mini:
                mini=i
            else:
                profit=max(profit,i-mini)
        return profit