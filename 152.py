class Solution(object):
    def maxProduct(self, nums):
        
        largest = big = small = nums[0]
        
        for n in nums[1:]:
            
            big, small = max(n, n*big, n*small), min(n, n*big, n*small)
            
            largest = max(largest, big)
            
        return largest
