class Solution(object):
    def longestArithSeqLength(self, A):
        
        dp = {}
        for i in xrange(len(A)):
            for j in xrange(i):
                dp[i, A[i] - A[j]] = dp.get((j, A[i] - A[j]), 1) + 1
        return max(dp.values())
