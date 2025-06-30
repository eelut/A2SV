# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, -1, -1)])
        res = 0
        while queue:
            node, parent, grandparent = queue.popleft()
            if grandparent % 2 == 0:
                res += node.val
            if node.left:
                queue.append((node.left, node.val, parent))
            if node.right:
                queue.append((node.right, node.val, parent))
        return res