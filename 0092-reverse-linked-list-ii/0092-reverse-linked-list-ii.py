# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외
        if not head or left==right:
            return head
        
        # start : 변경이 필요한 left의 바로 앞 지점
        # end : start.next
        # root : head보다 앞에 root를 만듦. 최종 결과는 root.next로 return 할 예정.
        root = start = ListNode(None)
        root.next = head
        # -> 이렇게 할당된 start, end는 끝까지 값이 변하지 않음. end는 reverse 부분의 맨 마지막이 될테니. 
        # start, end 지정
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right-left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
            
        return root. next