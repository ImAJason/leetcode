class Solution(object):
    def wordSubsets(self, A, B):

        d = collections.Counter()
        
        for b in B:
            for c, n in collections.Counter(b).items():
                d[c] = max(d[c], n)
                
        res = []
        for a in A:
            count = collections.Counter(a)
            if all(count[c]>=d[c] for c in d): 
                res.append(a)
                
        return res
                
            
        
