# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        pointer_fast,pointer_slow = dummy_head,dummy_head
        
        for i in range(n+1):
            pointer_fast = pointer_fast.next

        while pointer_fast:
            pointer_fast = pointer_fast.next
            pointer_slow = pointer_slow.next

        pointer_slow.next = pointer_slow.next.next

        return dummy_head.next