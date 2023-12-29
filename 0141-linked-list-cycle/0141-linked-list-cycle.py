# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow, fast를 사용하면 cycle이 있다면 언젠간 만난다는 점을 이용
        try:
            slow = head
            fast = head.next
            while slow is not fast: 
                # cycle이 있다면 언젠간 만남.
                slow = slow.next
                fast = fast.next.next
            return True
        except: 
            #slow/fast가 끝까지 가서 slow.next, fast.next.next이 없으면 에러가 나면서 except로 가게됨. cycle이 없다는 뜻
            return False