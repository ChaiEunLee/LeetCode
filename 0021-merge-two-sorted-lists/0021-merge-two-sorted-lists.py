# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # list1이 없거나 list1 값이 list2보다 크면 list1 기준으로 통합해야하니까 list2랑 list1을 바꾸기.
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        
        # list1.next, list2로 가서 다시 통합~
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1