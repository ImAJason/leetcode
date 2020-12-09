class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        
        to_routes = collections.defaultdict(set)
        
        for i, m in enumerate(routes):
            for j in m:
                to_routes[j].add(i)
                
        q = [(S,0)]
        visited = set([S])
        
        while q:
            
            x, cnt = q.pop(0)
            
            if x == T: return cnt
            
            for y in to_routes[x]:
                for z in routes[y]:
                    if z not in visited:
                        visited.add(z)
                        q.append((z, cnt+1))
                    
        return -1
                
                
            
        
