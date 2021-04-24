# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            self.set.add(root.val)
            self.check(root.left)
            self.check(root.right)
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.set=set()
        self.check(root)
        k =  list(sorted(self.set))
    
        try:
            return k[1]
        except:
            return -1
