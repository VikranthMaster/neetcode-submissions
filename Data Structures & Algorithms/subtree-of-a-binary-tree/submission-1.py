# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def findRoot(p,q):
            if not p:
                return False
            
            if p.val == q.val and isCorrect(p,q):
                return True
            
            return (findRoot(p.left, q) or findRoot(p.right,q))

        def isCorrect(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return(isCorrect(p.left, q.left) and isCorrect(p.right, q.right))

        return findRoot(root,subRoot)