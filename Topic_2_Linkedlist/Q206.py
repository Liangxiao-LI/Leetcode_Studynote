# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode()
        while head:
            dummy_head.val = head.val
            dummy_head = ListNode(next = dummy_head)
            head = head.next 

        return dummy_head.next