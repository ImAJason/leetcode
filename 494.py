class Solution(object):
    def findTargetSumWays(self, nums, S):
        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            tdp = collections.Counter()
            for i in (-1,1):
                for k in dp.keys():
                    tdp[k+i*n] +=dp[k]
            dp = tdp
        return dp[S]
