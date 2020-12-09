class Solution(object):
    def subarraySum(self, nums, k):
        
        d = {0:1}
        cnt, rsum = 0, 0
        
        for n in nums:
            
            rsum += n
            
            if rsum - k in d:
                cnt+=d[rsum-k]
            
            d[rsum] = d.get(rsum, 0) + 1
                
        return cnt
                
