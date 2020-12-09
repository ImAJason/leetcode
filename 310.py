class Solution(object):
    def findMinHeightTrees(self, n, edges):
        
        if n==1: return [0]
        
        neigh = collections.defaultdict(list)
        d = collections.defaultdict(int)
        
        for x, y in edges:
            neigh[x].append(y)
            neigh[y].append(x)
            d[x]+=1
            d[y]+=1
            
        unvisited = set(range(n))
        prelevel = []
        
        for i in range(n):
            if d[i] == 1:
                prelevel.append(i)
        
        while len(unvisited)>2:
            
            tmp = []
            for x in prelevel:
                unvisited.remove(x)
                
                for y in neigh[x]:
                    if y in unvisited:
                        d[y] -= 1
                        if d[y]==1:
                            tmp.append(y)
                    
            prelevel = tmp
            
        return prelevel
            
        
        
                             
                    
            
            
