
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        maping = {}
        curr = head
        while curr:
            maping[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            maping[curr].next = maping.get(curr.next)
            maping[curr].random = maping.get(curr.random)
            curr = curr.next

        return maping[head]