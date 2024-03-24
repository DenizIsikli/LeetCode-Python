# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    # Firstly, I call the isMirror function with the left and right children of the root.
    # In the isMirror function, if both left and right are None, I return True.
    # If only one of them is None, I return False.
    # If the values of the left and right nodes are not equal, I return False.
    # Otherwise, I recursively call the isMirror function with the left child of the left node
    # and the right child of the right node,
