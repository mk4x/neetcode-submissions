class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find all valleys and hills, calculate distance from valley to next hill, sum
        valleys, hills = [], []
        prices = [float('inf')] + prices + [-float('inf')]
        for i in range(1,len(prices)-1):
            if prices[i-1] > prices[i] <= prices[i+1]:
                valleys.append(i)
            if prices[i-1] < prices[i] >= prices[i+1]:
                hills.append(i)
        
        total = sorted(hills + valleys)
        #print(valleys, hills)
        res = sum(prices[hills[i]] - prices[valleys[i]] for i in range(min(len(hills), len(valleys))))
        return res