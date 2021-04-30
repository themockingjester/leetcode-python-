"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def check(self,root,level):
        if root:
            if level>self.max:
                self.max=level
            for i in root.children:
                self.check(i,level+1)
    def maxDepth(self, root: 'Node') -> int:
        self.max = 0
        self.check(root,1)
        return self.max
