class Solution(object):
    def canCross(self, stones):
        
        if stones[1]!=1: return False
        
        d = {x: set() for x in stones}
        d[1].add(1)
            
        for i in stones:
            for j in d[i]:
                for k in xrange(j-1, j+2):
                    if k>0 and i+k in d:
                        d[i+k].add(k)
                    
        return bool(d[stones[-1]])
