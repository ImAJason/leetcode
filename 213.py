class Solution(object):
    def rob(self, nums):
        
        def robber(nums):
            curr = pre = 0
            for x in nums:
                curr, pre = max(curr, pre+x), curr
            return curr
        
        n = len(nums)
        if n<2: return 0 if not nums else nums[0]
        return max(robber(nums[:n-1]), robber(nums[1:n]))
                
        
