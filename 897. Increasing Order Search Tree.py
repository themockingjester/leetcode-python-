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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.lis = []
        self.check(root)
        self.lis= sorted(self.lis)
        if len(self.lis)==0:
            return None
        head = TreeNode()
        head.val = self.lis[0]
        k = head
        del self.lis[0]
        while len(self.lis)!=0:
            p = TreeNode()
            p.val = self.lis[0]
            del self.lis[0]
            k.right = p
            k = k.right
        return head
