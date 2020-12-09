from collections import deque

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):

        def constructDict(wordList):
            d = {}
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i+1:]
                    d[s] = d.get(s,[]) + [word]
            return d
        
        def bfs_words(begin, end, d):
            q,visited = deque([(begin, 1)]), set()
            while q:
                word, cnt = q.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return cnt
                    
                    for i in range(len(word)):
                            s = word[:i] + '_' + word[i+1:]
                            pwords = d.get(s,[])
                            for pw in pwords:
                                if pw not in visited:
                                    q.append([pw,cnt+1])
            return 0
            
            
        
        d = constructDict(wordList)
        return bfs_words(beginWord, endWord, d)
