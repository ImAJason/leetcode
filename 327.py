class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        
        first = [0]
        for num in nums:
            first.append(first[-1] + num)
            
        def sort(l,r):
            
            m = (l+r)/2
            
            if l == m: return 0
            
            count = sort(l,m) + sort(m,r)
            
            i = j = m
            
            for left in first[l:m]:
                while i<r and first[i] - left < lower: i+=1
                while j<r and first[j] - left <= upper: j+=1
                count += (j-i)
                
            first[l:r] = sorted(first[l:r])
            return count
            
        return sort(0,len(first))
                
            
            
