# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        self.count = 0
        self.k = k
        self.value = 0
        def inorder(root: TreeNode):
            if not root:
                return

            inorder(root.left)
            self.count+=1
            if self.count == self.k:
                self.value = root.val
                return self.value
            inorder(root.right)
        inorder(root)
        return self.value

        