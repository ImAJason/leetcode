class Solution(object):
    def coinChange(self, coins, amount):
        
        dp = [0] + [float("inf")]*amount

        for i in range(1, amount+1):
            dp[i] = min(dp[i-c] if c<=i else float("inf") for c in coins) + 1

        return dp[-1] if dp[-1]!= float("inf") else -1

            
        
        
        
