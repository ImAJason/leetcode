class Solution(object):
    def isMatch(self, s, p):
        
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = True
        
        for i in range(len(p)):
            dp[i+1][0] = p[i] == '*' and dp[i-1][0]
            
            
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i]!='*':
                    dp[i+1][j+1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
                else:
                    dp[i+1][j+1] = dp[i][j+1] or dp[i-1][j+1]
                    if p[i-1] == s[j] or p[i-1] == '.':
                        dp[i+1][j+1] |= dp[i+1][j]
                        
        return dp[-1][-1]
                              
