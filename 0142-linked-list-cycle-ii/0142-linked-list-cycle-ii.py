from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None   # no cycle

        # Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow