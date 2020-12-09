class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.rank = 0
        
class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        def _insert(root, val):
            if not root:
                return TreeNode(val)
                
            if val<=root.val:
                root.left = _insert(root.left,val)
                root.rank += 1
            
            if val > root.val:
                root.right = _insert(root.right, val)
            
            return root
        
        self.root = _insert(self.root, val)
            
    def getRank(self, val):
        def _getRank(root, val):
            
            if not root: return 0
            
            if val <= root.val:
                return _getRank(root.left, val)
                
            if val > root.val:
                return 1 + root.rank + _getRank(root.right, val)
            
        return _getRank(self.root, val)    
    

class Solution(object):
    def countSmaller(self, nums):
        
        root, res = BST(), []
        
        for n in nums[::-1]:
            root.insert(n)
            res.insert(0, root.getRank(n))
            
        return res
        
        
