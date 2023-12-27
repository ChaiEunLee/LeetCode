# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        newhead = newlist = ListNode()
        
        while head1 and head2:
            # compare the value
            if head1.val >= head2.val:
                newlist.next = head2
                newlist= newlist.next
                head2 = head2.next
            else:
                newlist.next = head1
                newlist = newlist.next
                head1 = head1.next

        # 남은 리스트 통째로 붙이기
        if head1:
            newlist.next = head1
        if head2:
            newlist.next = head2
        
        return newhead.next