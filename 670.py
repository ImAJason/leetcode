class Solution(object):
    def maximumSwap(self, num):
        
        A = map(int,str(num))
        pos = {x:i for i,x in enumerate(A)}
        
        for i,x in enumerate(A):
            for j in range(9,x,-1):
                if pos.get(j,None) > i:
                    A[i],A[pos[j]] = A[pos[j]],A[i]
                    return int("".join(map(str,A)))
                
        return num
                
                
