class Solution(object):
    def candy(self, ratings):
        
        res = [1]*len(ratings)
        
        l=1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                l+=1
            else:
                l=1
            res[i] = l
            
        r=1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                r+=1
            else:
                r=1
            res[i] = max(res[i], r)
            
        return sum(res)
                
        
