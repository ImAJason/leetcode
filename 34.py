class Solution(object):
    def searchRange(self, nums, target):
        
        def bsearch(target):
            
            lo, hi = 0, len(nums)
            
            while lo<hi:
                
                mid = (lo+hi)/2
                
                if nums[mid]<target: lo = mid+1
                    
                else: hi = mid
                    
            return lo
        
        low = bsearch(target)
        
        return [low, bsearch(target+1)-1] if target in nums[low:low+1] else [-1,-1]
        
