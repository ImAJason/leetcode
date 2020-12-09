class Solution(object):
    def maxProfit(self, prices):
        
        if not prices: return 0
        
        b0 = b1 = -(prices[0])
        s0, s1, s2 = 0, 0, 0
        
        for i in range(1, len(prices)):
            b0 = max(b1, s2-prices[i])
            s0 = max(s1, b1+prices[i])
            
            b1= b0
            s1, s2 = s0, s1
            
        return s0
        
