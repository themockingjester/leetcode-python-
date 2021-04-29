# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            if root.val == self.key:
                
                self.check(root.right)
                self.check(root.left)
            else:
                self.lis.append(root.val)
                self.check(root.left)
                self.check(root.right)
                    
    
            
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def treemaker(root):
            if root:
                if root.val < i and root.right==None:
                    k = TreeNode()
                    k.val = i
                    root.right = k
                    return
                elif root.val < i and root.right!=None:
                    treemaker(root.right)
                elif root.val > i and root.left==None:
                    k = TreeNode()
                    k.val = i
                    root.left = k
                    return
                elif root.val > i and root.left!=None:
                    treemaker(root.left)
                    
        self.key = key
        self.lis = []
        self.check(root)
        print(self.lis)
        if len(self.lis)==0:
            return None
        head = TreeNode()
        head.val = self.lis[0]
        del self.lis[0]
        for i in self.lis:
            
            treemaker(head)
        return head
