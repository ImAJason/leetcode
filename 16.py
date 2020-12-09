class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        i = 0
        ans = nums[0]+nums[1]+nums[2]
             
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total == target: return total
                
                if abs(total-target) < abs(ans-target):
                    ans = total
                
                if total<target:
                    j+=1
                elif total>target:
                    k-=1
        
        return ans
            
