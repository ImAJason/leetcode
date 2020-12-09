class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        map = {0:-1}
        runningsum = 0
        
        for i in range(len(nums)):
            runningsum += nums[i]
            if k!=0:
                runningsum %= k
            
            if runningsum in map:
                if i-map[runningsum]>1:
                    return True
            else:
                map[runningsum] = i
            
        return False
        
        
