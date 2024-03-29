# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    # I check if the root is None and return None if it is.
    # I recursively call invertTree on the right child and assign it to the left child.
    # I recursively call invertTree on the left child and assign it to the right child.
    # I return the root.
    