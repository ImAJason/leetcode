class Solution(object):
    def findClosestElements(self, arr, k, x):
        
        l = r = bisect.bisect_left(arr, x)
        
        while (r-l)<k:
            
            if l == 0: return arr[:k]
            if r == len(arr): return arr[-k:]     
            
            if x-arr[l-1] <= arr[r]-x: l-=1
            else: r+=1
                
        return arr[l:r]

        
