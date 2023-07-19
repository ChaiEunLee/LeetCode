# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return null
        
        rootA, rootB = headA, headB
        
        while rootA != rootB:
            rootA = rootA.next if rootA else headB
            rootB = rootB.next if rootB else headA
        
        return rootA       