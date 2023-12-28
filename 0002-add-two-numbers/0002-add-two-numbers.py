# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse -> add -> reverse
        
        # 자릿수 법칙을 좀 잘 사용해야할듯.
        # reverse order로 저장되어있으니까 앞부터 더하면 됨.
        carrier = 0
        sumlisthead = sumlist = ListNode()
        
        while l1 and l2:
            num = l1.val + l2.val + carrier
            if num >= 10:
                carrier = 1
                num %= 10
            else:
                carrier = 0
            sumlist.next = ListNode(num)
            sumlist = sumlist.next
            l1 = l1.next
            l2 = l2.next
        
        # 리스트가 남으면
        while l1 or l2:
            # which list is left : l1 or l2
            if l1:
                num = l1.val + carrier
                l1 = l1.next
            if l2:
                num = l2.val + carrier
                l2 = l2.next
            
            # carrier
            if num >= 10:
                carrier = 1
                num %= 10
            else:
                carrier = 0
                
            sumlist.next = ListNode(num)
            sumlist = sumlist.next
        
        # if carrier = 1
        if carrier == 1:
            sumlist.next = ListNode(1)
            
        return sumlisthead.next
        