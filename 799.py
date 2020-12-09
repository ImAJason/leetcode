class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        
        dp = [[0] * k for k in xrange(1, 102)]
        dp[0][0] = poured
        
        for i in range(query_row+1):
            for j in range(i+1):
                amt = (dp[i][j] - 1.0) / 2.0
                if amt>0:
                    dp[i+1][j] += amt
                    dp[i+1][j+1]+= amt
                
        return min(1, dp[query_row][query_glass])
                
