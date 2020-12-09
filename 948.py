class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        
        points = ans = 0
        d = collections.deque(sorted(tokens))
        
        while d and (d[0]<=P or points):
            if d[0]<=P:
                P-=d.popleft()
                points+=1
            else:
                P+=d.pop()
                points-=1
            
            ans = max(ans, points)
            
        return ans
