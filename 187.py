class Solution(object):
    def findRepeatedDnaSequences(self, s):
        
        seen, res = set(), set()
        
        for i in xrange(len(s)-9):
            substring = s[i:i+10]
            
            if substring in seen:
                res.add(substring)
            else:
                seen.add(substring)
                
        return list(res)
        
