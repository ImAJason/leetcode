class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
       
        res = 0
        
        i = 0
        prod = 1
        
        for j in range(len(nums)):
            prod*=nums[j]
            while i<=j and prod>=k:
                prod/=nums[i]
                i+=1
                
            res+=(j-i+1)
                    
        return res
            
        
