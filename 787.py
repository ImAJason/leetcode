class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        
        graph = collections.defaultdict(dict)
        
        for u,v,w in flights:
            graph[u][v] = w
            
        q = [(0, src, 0)]
        
        while q:
            
            price, x, flights = heapq.heappop(q)
            if x == dst: return price
            if flights > K: continue
                
            for y in graph[x]:
                heapq.heappush(q, (price + graph[x][y], y, flights+1))      
            
        return -1
