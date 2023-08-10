"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        new_graph = dict()
        q = deque([node])
        
        new_graph[node.val] = Node(node.val, [])
        
        while q:
            v = q.popleft()
            for w in v.neighbors:
                if w.val not in new_graph:
                    new_graph[w.val] = Node(w.val, []) 
                    q.append(w)
                new_graph[v.val].neighbors.append(new_graph[w.val])
        return new_graph[node.val]
    