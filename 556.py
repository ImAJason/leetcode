class Solution(object):
    def nextGreaterElement(self, n):
        
        n = list(map(int, str(n)))
        
        i = len(n)-1
        while i>0 and n[i]<=n[i-1]:
            i-=1
        if i == 0: return -1
        
        j = i
        while j<len(n)-1 and n[j+1]>n[i-1]:
            j+=1
        
        n[i-1], n[j] = n[j], n[i-1]
        n[i:] = n[i:][::-1]
        
        n = int("".join(map(str, n)))
        
        return n if n<=((1<<31)-1) else -1
        
            
        
