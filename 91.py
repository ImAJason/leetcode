class Solution(object):
    def numDecodings(self, s):
        
        if not s: return 0
        
        n = len(s)
        
        p, pp = 1, 0
        
        for i in range(n-1, -1, -1):
            
            curr = p if s[i]!= '0' else 0
                
            if i<n-1 and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) < 7)):
                curr+=pp
                  
            p, pp = curr, p
            
        return p
            
                        
        
        
