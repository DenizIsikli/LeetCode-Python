# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 1

        if root.left is not None:
            count += self.countNodes(root.left)
        if root.right is not None:
            count += self.countNodes(root.right)

        return count

    # I first check if the root is None and return 0 if it is.
    # I initialize count to 1, since the root is not None.
    # I check if the left child is not None and recursively call countNodes on it.
    # I check if the right child is not None and recursively call countNodes on it.
    # I return the count.
