# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        in_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if in_left > in_right: 
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            
            idx = in_map[root_val]
            root.left = helper(in_left, idx - 1)
            root.right = helper(idx + 1, in_right)
            return root
        return helper(0, len(inorder) - 1)
