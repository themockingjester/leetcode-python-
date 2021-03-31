# this solution is not mine but love this solution so added

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, sum: list):
        if root is None:
            return
        self.helper(root.right, sum)
        sum[0] += root.val
        root.val = sum[0]
        self.helper(root.left, sum)
    def convertBST(self, root):
        self.helper(root, [0])
        return root
