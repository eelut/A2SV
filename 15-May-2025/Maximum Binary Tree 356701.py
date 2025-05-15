# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        largest=max(nums)
        idx=nums.index(largest)
        left,right=[],[]
        if idx >0:
            left=nums[:idx]
        if idx +1<=len(nums)-1:
            right=nums[idx+1:]
        
        root=TreeNode(val=largest)
        root.left=self.constructMaximumBinaryTree(left)
        root.right=self.constructMaximumBinaryTree(right)

        return root

        