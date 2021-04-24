# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            self.ctr+=1
            self.check(root.left)
            self.check(root.right)
    def countNodes(self, root: TreeNode) -> int:
        self.ctr = 0
        leftheight = 0
        rightheight = 0
        curr = root
        while curr:
            leftheight+=1
            curr = curr.left
        curr = root
        while curr:
            rightheight+=1
            curr = curr.right
        
        if  rightheight == leftheight:
            return 2**leftheight - 1
        else:
            self.check(root)
            return self.ctr
