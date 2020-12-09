class Solution(object):
    
    import collections
    
    def numberOfArithmeticSlices(self, A):
        
        dp = [collections.defaultdict(int) for _ in A]
        total = 0
        
        for i in xrange(len(A)):
            for j in xrange(i):
                dp[i][A[i]-A[j]] += 1
                
                if A[i]-A[j] in dp[j]:
                    dp[i][A[i]-A[j]] += dp[j][A[i]-A[j]]
                    
                    total += dp[j][A[i]-A[j]]
                    
        return total
