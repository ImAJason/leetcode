class Solution(object):
    def removeKdigits(self, num, k):
        
        stack = []
        
        for n in num:
            while k and stack and n<stack[-1]:
                stack.pop()
                k-=1
            stack.append(n)
            
        return ''.join(stack[:-k or None]).lstrip('0') or '0'
            
                    
        
