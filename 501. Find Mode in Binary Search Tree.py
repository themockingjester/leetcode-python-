# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            self.lis.append(root.val)
            self.check(root.left)
            self.check(root.right)
    def findMode(self, root: TreeNode) -> List[int]:
        self.lis = []
        self.check(root)
        k = set(self.lis)
        p = []
        for i in k:
            p.append(self.lis.count(i))
        u = max(p)
        j = []
        for i in k:
            if self.lis.count(i)==u:
                j.append(i)
        return j
