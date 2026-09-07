# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        def Issame(q1, q2):
            if not q1 and not q2:
                return True

            if not q1 or not q2 or q1.val != q2.val:
                return False
            return Issame(q1.left, q2.left) and Issame(q1.right, q2.right)

        if Issame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)