from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node to handle edge cases (e.g., removing head)
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow is now just before the node to delete
        slow.next = slow.next.next

        return dummy.next