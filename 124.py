# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        
        self.max = None
        
        def maxEnd(node):
            
            if not node: return 0
            
            left = maxEnd(node.left)
            right = maxEnd(node.right)
            
            self.max = max(self.max, node.val + left + right)
            
            return max(node.val + max(left, right), 0)
        
        maxEnd(root)
        return self.max
        
