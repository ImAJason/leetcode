class Solution(object):
    def getHint(self, secret, guess):
        
        cnt1, cnt2 = 0, 0
        nums = [0]*10
        
        for i in range(len(secret)):
            
            a, b = int(secret[i]), int(guess[i])
            
            if a == b:
                cnt1+=1
            
            else:
                
                if nums[a]<0:
                    cnt2+=1
                
                if nums[b]>0:
                    cnt2+=1
                    
                nums[a]+=1
                nums[b]-=1
                
        return "%sA%sB" % (cnt1, cnt2)
            
                
                
        
        
        """a, b = collections.Counter(secret), collections.Counter(guess)
        
        bulls = sum(i==j for i, j in zip(secret, guess))
        
        return '%sA%sB' % (bulls, sum((a&b).values()) - bulls)"""
    
    
                
