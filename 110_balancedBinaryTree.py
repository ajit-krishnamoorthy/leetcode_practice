class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0
    def height(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftHeight = self.height(root.left)
            rightHeight = self.height(root.right)
            if leftHeight < 0 or rightHeight < 0 or abs(leftHeight-rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1