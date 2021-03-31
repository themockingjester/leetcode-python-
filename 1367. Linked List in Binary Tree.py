# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check2(self,root,level):
        if root and self.stoppage==False:
            if root.val == self.lis[level]:
                if level==len(self.lis)-1:
                    self.stoppage=True
                    return
                self.check2(root.left,level+1)
                self.check2(root.right,level+1)
            else:
                return
    def check(self,root):
        if root and self.stoppage == False:
            if root.val==self.lis[0]:
                self.check2(root,0)
            self.check(root.left)
            self.check(root.right)           
                    
        
            
        
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        self.lis = []
        self.stoppage = False
        while head:
            self.lis.append(head.val)
            head = head.next
        
        self.check(root)
        return self.stoppage
            
        
