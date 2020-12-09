class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        
        for i,n in enumerate(nums[:len(nums)-k+1]):
            res.append(max(nums[i:i+k]))
            
        return res
        
