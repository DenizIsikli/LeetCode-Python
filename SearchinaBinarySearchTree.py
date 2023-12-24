class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None

        while root:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                break
        return root
