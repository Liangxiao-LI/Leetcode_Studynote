# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        while pointer:
            
            if pointer.next == None:
                return head

            val2 = pointer.next.val
            pointer.next.val = pointer.val
            pointer.val = val2
            pointer = pointer.next.next
        return head
