class Solution(object):
    def racecar(self, target):
        
        q = [(0,1)]
        visited = set([(0, 1)])
        cnt = 0
        
        while q:
            
            tmp = []
            cnt+=1
            
            for pos, spd in q:
                
                pos1, spd1 = pos+spd, spd*2
                if pos1 == target: return cnt
                
                pos2, spd2 = pos, 1 if spd<0 else -1
                
                tmp.append((pos1, spd1))
                
                if (pos2, spd2) not in visited:
                    visited.add((pos2, spd2))
                    tmp.append((pos2, spd2))
            
            q = tmp
                
        return -1
        
        
        
        
        
