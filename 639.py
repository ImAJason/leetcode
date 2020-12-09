class Solution(object):
    def numDecodings(self, s):
        
        MOD = 10**9 + 7
        p0, p1, p2 = 1,0,0
        
        for c in s:
            if c == '*':
                c0 = 9*p0 + 9*p1 + 6*p2
                c1 = p0
                c2 = p0
                
            else:
                c0 = (c>'0')*p0 + p1 + (c<='6')*p2
                c1 = (c=='1')*p0
                c2 = (c=='2')*p0
                
            p0, p1, p2 = c0 % MOD, c1, c2
            
        return p0 
