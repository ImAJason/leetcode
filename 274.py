class Solution(object):
    def hIndex(self, citations):
        
        n = len(citations)
        buckets = [0]*(n+1)
        
        for i in citations:
            if i >= len(citations):
                buckets[n]+=1
            else:
                buckets[i]+=1
                
        i = n-1
        while i >= 0:
            if buckets[i+1]>=i+1:
                return i+1
            buckets[i] += buckets[i+1]
            i-=1
            
        return 0
                
        
