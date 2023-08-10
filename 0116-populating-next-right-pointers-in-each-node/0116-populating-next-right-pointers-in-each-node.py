"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # there always the case where root node is None
        if not root:
            return root
            
        queue = collections.deque([root])
        visited = []
        while queue:
            prev = None
            # number of nodes in the level - when we want to go over all the elements
            size = len(queue)
            while size>0:
                node = queue.popleft()
                # setting the next pointer
                # my next pointer is previous, set previous as me for the next node
                node.next = prev
                prev = node
                # For its child
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                size -= 1
        return root