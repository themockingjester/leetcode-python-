# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,content):
        if root:
            print(content)
            
            
            content.append(root.val)

            sumis = sum(content)
            if sumis == self.target:
                if root.left==None and root.right==None:
                    print("ok")
                    self.lis.append(content)
                else:
                    self.check(root.left,content.copy())

                    self.check(root.right,content)

            else:
                self.check(root.left,content.copy())

                self.check(root.right,content)
                        

    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        content = []
        self.target = targetSum
        self.lis=[]
        if root:
            self.check(root,content)
        return self.lis
