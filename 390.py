class Solution(object):
    def lastRemaining(self, n):
        
        return self.leftToright(n)
    
    def leftToright(self,n):
        
        if n==1: return 1
        
        return 2 * self.rightToleft(n/2)
        
    def rightToleft(self,n):
        
        if n==1: return 1
        
        if n%2 == 0: return (2*self.leftToright(n/2)) - 1
        
        else: return 2 * self.leftToright(n/2)
    
    
    
        """nums = range(1,n+1)
        
        while len(nums) > 1 :
            nums = nums[1::2][::-1]
        
        return nums[0]"""
