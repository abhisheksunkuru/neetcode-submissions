class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        suffix_max = [0]*length

        j = length-1
        maximum = 0
        while j >=0:
            if j== length-1:
                maximum = prices[j]
            else:    
                suffix_max[j] = maximum     
                if prices[j] > maximum:
                    maximum = prices[j]
            j -= 1
        print(suffix_max)
        max_profit = 0
        for i in range(0, length):
            profit = suffix_max[i]-prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit                
