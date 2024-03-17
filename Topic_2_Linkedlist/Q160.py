# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA,lenB = 0,0
        pointerA = headA
        while pointerA:
            lenA += 1
            pointerA = pointerA.next
        pointerB = headB
        while pointerB:
            lenB += 1
            pointerB = pointerB.next
        
        pointerA,pointerB = headA,headB

        if lenA > lenB:
            for i in range(lenA - lenB):
                pointerA = pointerA.next
        else:
            for i in range(lenB - lenA):
                pointerB = pointerB.next
        
        while pointerA and pointerB:
            if pointerA == pointerB:
                return pointerA
            else:
                pointerA = pointerA.next
                pointerB = pointerB.next