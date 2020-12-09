class Solution(object):
    def minWindow(self, s, t):
        
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        
        for j,c in enumerate(s,1):
            missing -= need[c]>0
            need[c] -= 1
    
            if not missing:
                while need[s[i]]<0 and i<j:
                    need[s[i]]+=1
                    i+=1
                    
                if not J or j-i < J-I:
                    J, I = j, i
                
        return s[I:J]
        
