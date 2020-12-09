class Solution(object):
    def wordBreak(self, s, wordDict):
        
        memo = {}
        return self.construct(s, wordDict, memo)
    
    def construct(self, s, wordDict, memo):
        
        if not s: return []
        if s in memo: return memo[s]
        
        res = []
        
        for w in wordDict:
            
            if s.startswith(w):
                
                if not s.startswith(w):
                    continue
                
                if len(w) == len(s):
                    res.append(w)
                
                else:
                    restof = self.construct(s[len(w):], wordDict, memo)
                    for r in restof:
                        res.append(w + " " + r)
        
        memo[s] = res
        return memo[s]
