class Solution(object):
    def isValid(self, a, b):
        
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt +=1
        return cnt == 1
    
    def minMutation(self, start, end, bank):
    
        cnt = 0
        visited = []
        q = [[start, start, cnt]]
        
        while q:
            curr, prev, cnt = q.pop(0)
            if curr == end:
                return cnt
            
            for dna in bank:
                if self.isValid(curr, dna) and dna!= prev and dna not in visited:
                    visited.append(dna)
                    q.append([dna, curr, cnt+1])
            
        return -1
