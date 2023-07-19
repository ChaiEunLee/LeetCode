# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: #node가 1개 일 때
            return None
        
        #slow.next가 없을 때 오류가 나지 않기 위해서 fast를 더 앞에서 시작함.
        slow, fast = head, head.next.next
        
        while fast and fast.next: #이 조건이 중요!
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next
        
        return head