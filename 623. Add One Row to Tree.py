# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,level):
        if root:
            if self.depth == 1:
                node1 = TreeNode(self.value)
                node1.left = root
                
                self.root  = node1
                return
            if level == self.depth-1:
                node1 = TreeNode(self.value)
                node2 = TreeNode(self.value)
                node1.left = root.left
                node2.right = root.right
                root.left = node1
                root.right = node2
                return 
            else:
                if root.left:
                    self.check(root.left,level+1)
                if root.right:
                    self.check(root.right,level+1)
            
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        self.depth = depth
        self.value = val
        self.root = root
        if self.root:
            self.check(self.root,1)
        return self.root
        
