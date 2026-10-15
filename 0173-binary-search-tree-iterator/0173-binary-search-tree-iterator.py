# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # Push all leftmost nodes onto the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # The top of the stack is the next smallest element
        node = self.stack.pop()
        # Process its right subtree by pushing all leftmost nodes
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0