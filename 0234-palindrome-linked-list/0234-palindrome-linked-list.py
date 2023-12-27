# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        
        while fast and fast.next: #fast.next를 꼭 넣어줘야함. 
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next #slow를 움직이면서 reverse list로 동시에 만들어줌.
        if fast:
            slow = slow.next
            
        # Check palindrome
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev