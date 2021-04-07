# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            leftchildcoins = self.check(root.left)
            rightchildcoins = self.check(root.right)
            k = abs(leftchildcoins)+abs(rightchildcoins)
            self.res+=k
            return leftchildcoins+rightchildcoins+root.val-1
        else:
            return 0
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        self.check(root)
        return self.res
        
