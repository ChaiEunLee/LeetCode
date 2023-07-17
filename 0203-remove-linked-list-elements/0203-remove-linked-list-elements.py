# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = cur = head
        
        if not cur:
            return head
        while cur:
            if cur.val == val:
                dummy.next = cur.next
                cur = cur.next
            else:
                if cur.next and cur.next.val == val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
        return dummy.next