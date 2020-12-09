class Solution(object):
    def findNumberOfLIS(self, nums):
        
        if not nums: return 0
        
        dp, dp2 = [1]*len(nums), [1]*len(nums)

        ans, maxval = 1, 1
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        dp2[i] = dp2[j] 
            
                    elif dp[j]+1 == dp[i]:
                        dp2[i]+=dp2[j]
                            
            if dp[i] > maxval: 
                maxval, ans = dp[i], dp2[i]
            
            elif dp[i] == maxval:
                ans+=dp2[i]
                    
        return ans
