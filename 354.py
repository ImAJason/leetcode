class Solution(object):
    def maxEnvelopes(self, envelopes):
        
        end = [None]*len(envelopes)
        
        envelopes = sorted(envelopes, key = lambda (w,h): (w,-h))
        
        hi = 0
        
        for _,h in envelopes:
            
            i = bisect.bisect_left(end, h, hi = hi)
            end[i] = h
            hi += i == hi
            
        return hi
        
