# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return (1+max(self.maxDepth(root.left), self.maxDepth(root.right)))

    # Firstly I check if the root (TreeNode) exists. If it does, I return the max of tree nodes between left and right
    # and see which one has the most nodes, hereby returning the max depth