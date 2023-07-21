# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        slow = head
        fast = head.next.next
        current = head.next
        answer = []
        i = 1
        previ = -100000
        minDistance = 100000
        
        while current.next:
            if (current.val - slow.val < 0 and current.val - fast.val < 0) or (current.val - slow.val > 0 and current.val - fast.val > 0):
                if i - previ < minDistance:
                    minDistance = i - previ
                answer.append(i)
                previ = i
            current = current.next
            slow = slow.next
            fast = fast.next
            i += 1

        if len(answer) < 2:
            minDistance = -1
            maxDistance = -1
        else:
            maxDistance = answer[len(answer)-1] - answer[0]

        return [minDistance, maxDistance]
    