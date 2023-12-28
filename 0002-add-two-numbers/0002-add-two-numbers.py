# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 몫과 나머지 계산
            carry, val = divmod(sum+carry,10)
            # divmod 안 쓸거면 일의자리부터 계산해야함. 
#            val = (sum+carry) % 10 #일의자리
#            carry = (sum+carry) // 10 #십의자리
            head.next = ListNode(val)
            head = head.next
            
        return root.next
            
        