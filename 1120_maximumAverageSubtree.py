# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAvg = 0.0
        def traverse(root: Optional[TreeNode]) -> [int, int]:
            if not root:
                return [0, 0]
            leftNode, leftCount = traverse(root.left)
            rightNode, rightCount = traverse(root.right)
            self.maxAvg = max(self.maxAvg, (leftNode+rightNode+root.val)/(leftCount+rightCount+1))
            return [leftNode+rightNode+root.val, leftCount+rightCount+1]
        traverse(root)
        return self.maxAvg