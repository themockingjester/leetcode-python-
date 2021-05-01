# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            if root.val <= self.high and root.val>=self.low:
                self.sum+=root.val
            self.check(root.left)
            self.check(root.right)
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.sum = 0
        self.check(root)
        return self.sum
