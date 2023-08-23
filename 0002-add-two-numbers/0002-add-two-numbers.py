# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = n = ListNode(0) #나중에 새로운 list의 맨 앞(root.next)을 반환해야해서
        while l1 or l2 or carry: #carry만 남을 수도 있으니까
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
               
            #carry, v = divmod((v1+v2+carry), 10)
            # val부터 해야지 carry부터 계산하면 안 됨!
            v = (v1+v2+carry) % 10 #일의자리
            carry = (v1+v2+carry) // 10 #십의자리
            
                        
            # n이 first node고 n.next에 계속 하나씩 넣으면서 앞에다가 붙여주는 형식
            n.next = ListNode(v)
            n = n.next
        
        return root.next
    
    