# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder 시작 = root
        # inorder 시작 = 왼쪽 leaf node
        if inorder:
            # preorder 결과는 inorder 분할 인덱스
            index = inorder.index(preorder.pop(0)) #preorder 시작은 root라서 inorder의 중간으로 가른다. 
            
            # inorder 결과 divide & conquer
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            
            return node