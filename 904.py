class Solution(object):
    def totalFruit(self, tree):
        
        ans = curr = count_b = a = b = 0
        
        for t in tree:
            
            curr = curr + 1 if t in (a, b) else count_b + 1
            count_b = count_b + 1 if t==b else 1
            if t!=b: a, b = b, t
            
            ans = max(ans, curr)
            
        return ans
        
