# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True
            
            left = dfs(p.left) == dfs(q.left)
            right = dfs(p.right) == dfs(q.right)

            if left == right:
                return True
            else:
                return False
            
        dfs(p,q)
        