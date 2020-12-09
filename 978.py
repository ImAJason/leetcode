class Solution(object):
    def maxTurbulenceSize(self, A):
        
        res = inc = dec = 1
        for i in xrange(1, len(A)):
            
            if A[i] < A[i-1]: 
                dec, inc = inc+1, 1
            
            elif A[i] > A[i-1]: 
                inc, dec = dec+1, 1
            
            else:
                inc, dec, = 1, 1
            
            res = max(res, inc, dec)
            
        return res
