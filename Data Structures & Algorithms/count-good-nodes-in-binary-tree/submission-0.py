# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxSeen):

            if not root:
                return 0
            newMax = max(root.val,maxSeen)
            goodPath = dfs(root.left, newMax) + dfs(root.right, newMax)

            if root.val >= maxSeen:
                return 1 + goodPath
            return goodPath
        
        return dfs(root, float("-inf"))
        