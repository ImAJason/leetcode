class Solution(object):
    def palindromePairs(self, words):
        
        d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        
        for i, w in enumerate(words):
            for j in xrange(len(w)+1):
                prefix, suffix = w[:j], w[j:]
                
                if prefix in d and i!=d[prefix] and suffix==suffix[::-1]:
                    res.append([i, d[prefix]])
                    
                if j>0 and suffix in d and i!=d[suffix] and prefix==prefix[::-1]:
                    res.append([d[suffix],i])
                    
        return res
    
