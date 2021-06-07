# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self,root1,root2):
        if root1 and root2 and self.resume:
            if root1==self.target:
                self.ans = root2
                self.resume=False
            else:
                self.check(root1.left,root2.left)
                self.check(root1.right,root2.right)
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.target = target
        self.ans = None
        self.resume = True
        self.check(original,cloned)
        return self.ans
