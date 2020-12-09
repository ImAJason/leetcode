class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        
        nums = range(1, maxChoosableInteger+1)
        d = {}
        
        def dfs(nums,desiredTotal):
            
            s = str(nums)
            if s in d:
                return d[s]
            
            if nums[-1] >= desiredTotal:
                return True
            
            for i in range(len(nums)):
                
                if not dfs(nums[:i] + nums[i+1:], desiredTotal-nums[i]):
                    d[s] = True
                    return True
                
            d[s] = False
            return False
        
        return dfs(nums, desiredTotal)
                
