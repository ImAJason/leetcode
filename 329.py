class Solution(object):
    def longestIncreasingPath(self, matrix):
        
        if not matrix: return 0
        
        m,n = len(matrix), len(matrix[0])
        
        def dfs(i, j):
            
            if not dp[i][j]: 
                
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i and matrix[i-1][j] < val else 0, 
                    dfs(i+1, j) if i<m-1 and matrix[i+1][j] < val else 0, 
                    dfs(i, j-1) if j and matrix[i][j-1] < val else 0, 
                    dfs(i, j+1) if j<n-1 and matrix[i][j+1] < val else 0)
                
            return dp[i][j]
        
        dp = [[0]*n for _ in range(m)]
        ans = 0
        
        return max(dfs(i,j) for i in range(m) for j in range(n))
        
        
        """for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
                
        return ans"""
        
            
