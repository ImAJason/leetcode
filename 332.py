class Solution(object):
    def findItinerary(self, tickets):
        
        d = collections.defaultdict(list)
        
        for t in sorted(tickets, key = lambda x: x[1], reverse = True):
            d[t[0]].append(t[1])
            
        def dfs(depart):
            
            while d[depart]:
                dfs(d[depart].pop())
                
            res.append(depart)
                
        res = []
        dfs("JFK")
            
        return res[::-1]
        
