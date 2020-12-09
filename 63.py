class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        dp = [0]*len(obstacleGrid[0])
        dp[0] = 1
                
        for i in xrange(len(obstacleGrid)):
            for j in xrange(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j>0:
                    dp[j] += dp[j-1]

        return dp[-1]
        
