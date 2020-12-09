class Solution(object):
    def carFleet(self, target, position, speed):
        
        time = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        
        res, curr = 0, 0
        for t in time[::-1]:
            if t > curr:
                res+=1
                curr = t
                
        return res
                
            
        
