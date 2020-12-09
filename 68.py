class Solution(object):
    def fullJustify(self, words, maxWidth):
        
        res, cur, numLength = [], [], 0
        
        for w in words:
            
            
            if numLength + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - numLength):
                    cur[i%(len(cur)-1 or 1)] += ' '
                    
                res.append(''.join(cur))
                cur, numLength = [], 0
                
                
            numLength += len(w)
            cur += [w]
            
        return res + [' '.join(cur).ljust(maxWidth)]
