class Solution(object):
    def makesquare(self, nums):
        
        if not nums or len(nums)<4: return False
        
        numsum = sum(nums)
        if numsum % 4 != 0: return False
        
        nums.sort(reverse = True)
        target = [numsum/4]*4
        
        return self.dfs(nums, 0, target)
        
    def dfs(self, nums, index, target):
        
        if index == len(nums): return True
        
        for i in range(4):
            if target[i]>=nums[index]:
                target[i]-=nums[index]
                if self.dfs(nums, index+1, target): return True
                target[i]+=nums[index]
                
        return False
