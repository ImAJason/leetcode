class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        
        q = []
        
        def push(i, j):
            
            if i< len(nums1) and j<len(nums2):
                heapq.heappush(q, [nums1[i] + nums2[j], i, j])
        
        push(0,0)
        
        cnt = 0
        res = []
        while q and cnt<k:
            _, i, j = heapq.heappop(q)
            res.append([nums1[i],nums2[j]])
            cnt += 1
            
            push(i, j+1)
            
            if j == 0:
                push(i+1,j)
        
        return res
     
