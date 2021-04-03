"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def check(self,root):
        if root:
            self.lis.append(root.val)
            
            for i in root.children:
                self.check(i)
    def preorder(self, root: 'Node') -> List[int]:
        self.lis = []
        self.check(root)
        return self.lis
        
