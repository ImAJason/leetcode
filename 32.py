class Solution(object):
    def longestValidParentheses(self, s):
        
        s = ')' + s
        stack = [0]
        res = 0
        
        for i in xrange(1, len(s)):
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
                
        return res
            
                    
