# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._temp_(root, targetSum, 0)

    def _temp_(self, root: Optional[TreeNode], targetSum: int, sum: int) -> bool:
        if not root:
            return False
        sum += root.val
        if not root.left and not root.right:
            return sum == targetSum
        return self._temp_(root.left, targetSum, sum) or self._temp_(root.right, targetSum, sum)

    # Firstly, I call the _temp_ function with the root, targetSum, and 0.
    # In the _temp_ function, if the root is None, I return False.
    # If not, I add the value of the current node to the sum.
    # If the current node is a leaf node, I check if the sum is equal to the targetSum.
    # If so, I return True.
    # Otherwise, I return the result of the recursive calls on the left and right children of the current node.
    # If either of them returns True, the function will return True.
